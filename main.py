from fastapi import FastAPI, Query, HTTPException
from typing import Optional
from app.models.colleges import CollegeScreen, College, GrantsScreen, Grant
from app.models.home_model import HomeScreen
from app.data.home_data import university_info, president_message, university_info_en, president_message_en
from app.data.college_data import grants_list, general_rules, colleges_data, grants_list_ar, general_rules_ar, colleges_data_ar
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key) if supabase_url and supabase_key else None

app = FastAPI(title="Banha National University - Colleges API")

@app.get("/")
async def root():
    return {"message": "API is live! Visit /docs for interactive Swagger UI."}
#############   Home Page  ############

@app.get("/home", response_model=HomeScreen)
async def get_home(
    username: Optional[str] = Query(None, description = "Username for Greeting"),
    lang: str = Query("arabic", description = "Language: arabic or english")
):
    if supabase:
        try:
            response = supabase.table("home").select("*").eq("lang", lang).execute()

            if response.data:  
                home_row = response.data[0]
                welcome_msg = None
                if lang == "arabic" and username:
                    welcome_msg = f"مرحبا بك يا {username} في جامعة بنها الأهلية"
                elif lang == "english" and username:
                    welcome_msg = f"Welcome {username} to Banha National University"
              

                return HomeScreen(
                    welcome=welcome_msg,
                    university=home_row["university_info"],      
                    president_message=home_row["president_message"], 
                    fromDB=True
                )

        except Exception as e:
            print("ERROR fetching from Supabase:", e)

    if lang == "english":
        uni_data = university_info_en
        pres_msg = president_message_en
        welcome_msg = f"Welcome {username} to Banha National University 🎓" if username else None
        
    elif lang == "arabic":
        uni_data = university_info
        pres_msg = president_message
        welcome_msg = f"مرحبًا يا {username} في جامعة بنها الأهلية 🎓" if username else None

    else:
        raise HTTPException(
        status_code=400,
        detail="Invalid language. Supported values are 'arabic' and 'english'."
    )
    
    result = HomeScreen(
        welcome=welcome_msg,
        university=uni_data,
        president_message=pres_msg,
        fromDB= False
    )

    return result


##########       Colleges Page      #############


@app.get("/colleges", response_model=CollegeScreen)
async def get_colleges(
    lang: str = Query("arabic", description="arabic or english")
):
    if supabase:
        try:
            response = supabase.table('colleges').select('*').eq("lang", lang).execute()
            if response.data:
                db_colleges = []
                for college in response.data:
                    programs_resp = supabase.table('programs').select('name').eq('college_id', college['id']).eq("lang", lang).execute()
                    programs = [p['name'] for p in programs_resp.data] if programs_resp.data else []
                    
                    db_colleges.append(College(
                        name=college['name'],
                        programs=programs,
                        tuition_fee=college['tuition_fee']
                    ))
                
                return CollegeScreen(
                    colleges=db_colleges,
                    total_colleges=len(db_colleges),
                    fromDB=True
                )
        except Exception as e:
            print(f"Error fetching from Supabase: {e}")
            
    if lang == "english":
        data = list(colleges_data.values())
        return CollegeScreen(colleges=data, total_colleges=len(colleges_data), fromDB=False)
    elif lang== "arabic":
        data = list(colleges_data_ar.values())
        return CollegeScreen(colleges=data, total_colleges=len(colleges_data), fromDB=False)
    else:
        raise HTTPException(
        status_code=400,
        detail="Invalid language. Supported values are 'arabic' and 'english'."
    )

    

@app.get("/colleges/{college_id}", response_model=dict)
async def get_college(college_id: str,
    lang: str= Query("arabic", description="arabic or english")
    ):
    if supabase:
        try:
            response = supabase.table('colleges').select('*').eq('id', college_id).eq("lang", lang).execute()
            if response.data:
                college = response.data[0]
                programs_resp = supabase.table('programs').select('name').eq('college_id', college_id).eq("lang",lang).execute()
                programs = [p['name'] for p in programs_resp.data] if programs_resp.data else []
                
                return {
                    **college,
                    "programs": programs,
                    "fromDB": True
                }
        except Exception as e:
            print(f"Error fetching from Supabase: {e}")
    
    if lang == "english":
        college = colleges_data.get(college_id)
        return {**college.dict(), "fromDB": False}
    elif lang== "arabic":
        college = colleges_data_ar.get(college_id)
        return {**college.dict(), "fromDB": False}
    else:
        raise HTTPException(
            status_code=404,
            detail="Enter valid credentials")
    

@app.get("/grants", response_model=GrantsScreen)
async def get_grants(
    lang:str= Query("arabic",description="arabic or english")
):
    if supabase:
        try:
            grants_resp = supabase.table('grants').select('*').eq("lang",lang).execute()
            rules_resp = supabase.table('rules').select('text').eq("lang",lang).execute()
            
            if grants_resp.data and rules_resp.data:
                return GrantsScreen(
                    grants=[Grant(**g) for g in grants_resp.data],
                    rules=[r['text'] for r in rules_resp.data],
                    fromDB=True
                )
        except Exception as e:
            print(f"Error fetching from Supabase: {e}")
    
    if lang == "english":
        return GrantsScreen(grants=grants_list, rules=general_rules, fromDB=False)
    elif lang== "arabic":
       return GrantsScreen(grants=grants_list_ar, rules=general_rules_ar, fromDB=False)
    else:
        raise HTTPException(
        status_code=400,
        detail="Invalid language. Supported values are 'arabic' and 'english'."
    )
    
