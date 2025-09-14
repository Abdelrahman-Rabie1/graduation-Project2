from app.models.home_model import UniversityOverview
from app.models.home_model import PresidentMessage

president_message = PresidentMessage(
    greeting="بِسْمِ اللَّهِ ... أهلًا بكم في الموقع الرسمي لجامعة بنها الأهلية",
    image_url="https://bnu.edu.eg/files/85666_1726150758.jpg",
    content="إن التاريخ هو أصل الحاضر ... جامعة بنها الأهلية تستهدف إعداد جيل جديد ...",
    closing="وفي الختام أمنياتي بالتوفيق والنجاح.\nحفظ الله مصر.",
    president_name="أ.د تامر سمير - رئيس الجامعة"
)

faculties_list = [
    "كلية الطب البشرى","كلية طب الأسنان","كلية العلاج الطبيعى","كلية الهندسة",
    "كلية تكنولوجيا العلوم الصحية التطبيقية","كلية الأقتصاد وإدارة الأعمال",
    "كلية علوم الحاسب","كلية الفنون البصرية","كلية الطب البيطرى","كلية علوم الطاقة"
]

university_info = UniversityOverview(
    name="جامعة بنها الأهلية",
    description="جامعة أهلية غير هادفة للربح (...) تضم 10 كليات.",
    image_url="https://bnu.edu.eg/files/26859_1659649382.jpg",
    established="قرار رئيس الجمهورية 369 لسنة 2022",
    faculties=faculties_list,
    programs_count=25,
    campus="مساحة 40 فدان مع مرافق متطورة",
    buildings=[
        "المبنى الإداري","6 مباني أكاديمية","مبنى المعامل المركزية",
        "2 مبنى للورش","منطقة ترفيهية","مسرح","مكتبة شاملة"
    ],
    vision="تعتمد تقنيات التعليم الحديثة وتنافس عالميًا مع الحفاظ على الهوية المصرية."
)


#########  English ##########

president_message_en = PresidentMessage(
    greeting="In the name of God, the Most Gracious, the Most Merciful... Welcome to the official website of Banha National University",
    image_url="https://bnu.edu.eg/files/85666_1726150758.jpg",
    content="History is the origin of the present and the gateway to the future. Banha National University aims to prepare a new generation of students, equipped with knowledge, creativity, and the ability to compete globally while maintaining national values.",
    closing="In conclusion, I wish you all success and excellence.\nMay God bless Egypt.",
    president_name="Prof. Dr. Tamer Samir - President of the University"
)


faculties_list_en = [
    "Faculty of Medicine", "Faculty of Dentistry", "Faculty of Physical Therapy", "Faculty of Engineering",
    "Faculty of Applied Health Sciences Technology", "Faculty of Economics and Business Administration",
    "Faculty of Computer Science", "Faculty of Visual Arts", "Faculty of Veterinary Medicine", "Faculty of Energy Sciences"
]

university_info_en = UniversityOverview(
    name="Banha National University",
    description="A non-profit smart university (...) consisting of 10 faculties.",
    image_url="https://bnu.edu.eg/files/26859_1659649382.jpg",
    established="Presidential Decree No. 369 of 2022",
    faculties=faculties_list_en,
    programs_count=25,
    campus="Covers 40 acres with advanced facilities",
    buildings=[
        "Administrative Building", "6 Academic Buildings", "Central Laboratories Building",
        "2 Workshop Buildings", "Recreational Area", "Theater", "Comprehensive Library"
    ],
    vision="Adopts modern educational technologies, competes globally while preserving Egyptian identity."
)