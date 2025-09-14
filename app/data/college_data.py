from app.models.colleges import CollegeScreen, College, Grant
from typing import Dict


grants_list = [
    Grant(
        title="Excellence Grants",
        details="Full scholarships for top students + discounts (25%, 20%, 15%, 10%) according to rank. Conditions apply."
    ),
    Grant(
        title="Sports Excellence Grants",
        details="Discounts for medal winners: International (70%, 50%, 25%), Arab/African (30%, 20%, 10%)."
    ),
    Grant(
        title="Creative & Research Grants",
        details="Special discounts for distinguished students in research and innovation as approved by the university council."
    ),
    Grant(
        title="Tuition Fee Reductions",
        details="50% for sons of martyrs, 20% for staff children, 10% siblings, disability-based discounts."
    ),
    Grant(
        title="Social Support",
        details="5%–25% tuition fee reduction for students facing sudden financial hardships."
    )
]

general_rules = [
    "Grants and discounts apply only to Egyptian students.",
    "Discounts apply only to tuition fees and not to administrative fees.",
    "Excellence grants apply in the following year.",
    "It is not permissible to combine more than one grant; only the highest applies.",
    "Grants or discounts are not applied retroactively."
]

colleges_data: Dict[str, College] = {
    "medicine": College(
        name="College of Medicine",
        programs=["General Medicine"],
        tuition_fee=155000,
    ),
    "dentistry": College(
        name="College of Dentistry",
        programs=["General Dentistry"],
        tuition_fee=125000,
    ),
    "physical therapy": College(
        name="College of Physical Therapy",
        programs=["Physical Therapy"],
        tuition_fee=110000,
    ),
    "veterinary": College(
        name="College of Veterinary Medicine",
        programs=["Veterinary Medicine"],
        tuition_fee=80000,
    ),
    "engineering": College(
        name="College of Engineering",
        programs=[
            "Engineering of Communication Systems",
            "Mechatronics Engineering",
            "Housing and Community Design",
            "Construction Engineering",
            "Medical Engineering",
            "Manufacturing & Materials Engineering"
        ],
        tuition_fee=75000,
    ),
    "computer science": College(
        name="College of Computer Sciences",
        programs=[
            "Artificial Intelligence & Machine Learning",
            "Computational Linguistics",
            "Data Science",
            "Program Development & Applications",
            "Virtual Reality & Augmented Reality"
        ],
        tuition_fee=75000,
    ),
    "visual arts": College(
        name="College of Visual Arts & Design",
        programs=["Interior design and furniture", "Media and advertising"],
        tuition_fee=60000,
    ),
    "business": College(
        name="College of Business and Economics",
        programs=[
            "International Business & Relations Management",
            "International Economics & Finance",
            "Accounting and Business Informatics",
            "Digital Marketing and E-Business",
            "Insurance and statistics"
        ],
        tuition_fee=50000,
    ),
    "energy": College(
        name="College of Energy Sciences",
        programs=["Fossil Fuel Energy", "Renewable Energy", "Nuclear Energy"],
        tuition_fee=45000,
    ),
}


################## Arabic  ################################


grants_list_ar = [
    Grant(
        title="منح التفوق",
        details="منح دراسية كاملة للطلاب الأوائل + خصومات (25%، 20%، 15%، 10%) حسب الترتيب. تطبق الشروط."
    ),
    Grant(
        title="منح التفوق الرياضي",
        details="خصومات للفائزين بالميداليات: دولي (70%، 50%، 25%)، عربي/إفريقي (30%، 20%، 10%)."
    ),
    Grant(
        title="منح الإبداع والبحث",
        details="خصومات خاصة للطلاب المتميزين في البحث والابتكار كما يقرها مجلس الجامعة."
    ),
    Grant(
        title="تخفيضات المصروفات الدراسية",
        details="50% لأبناء الشهداء، 20% لأبناء العاملين، 10% للإخوة، خصومات لذوي الإعاقة."
    ),
    Grant(
        title="الدعم الاجتماعي",
        details="تخفيض من 5% إلى 25% من المصروفات للطلاب الذين يواجهون أزمات مالية مفاجئة."
    )
]

general_rules_ar = [
    "تطبق المنح والخصومات على الطلاب المصريين فقط.",
    "تطبق الخصومات على المصروفات الدراسية فقط وليس على الرسوم الإدارية.",
    "تطبق منح التفوق في العام التالي.",
    "لا يجوز الجمع بين أكثر من منحة؛ يطبق فقط الأعلى.",
    "لا تطبق المنح أو الخصومات بأثر رجعي."
]

colleges_data_ar: Dict[str, College] = {
    "medicine": College(
        name="كلية الطب",
        programs=["الطب البشري"],
        tuition_fee=155000,
    ),
    "dentistry": College(
        name="كلية طب الأسنان",
        programs=["طب الأسنان العام"],
        tuition_fee=125000,
    ),
    "physical therapy": College(
        name="كلية العلاج الطبيعي",
        programs=["العلاج الطبيعي"],
        tuition_fee=110000,
    ),
    "veterinary": College(
        name="كلية الطب البيطري",
        programs=["الطب البيطري"],
        tuition_fee=80000,
    ),
    "engineering": College(
        name="كلية الهندسة",
        programs=[
            "هندسة نظم الاتصالات",
            "هندسة الميكاترونكس",
            "الإسكان وتصميم المجتمع",
            "الهندسة الإنشائية",
            "الهندسة الطبية",
            "هندسة التصنيع والمواد"
        ],
        tuition_fee=75000,
    ),
    "computer science": College(
        name="كلية علوم الحاسب",
        programs=[
            "الذكاء الاصطناعي وتعلم الآلة",
            "اللغويات الحاسوبية",
            "علم البيانات",
            "تطوير البرمجيات والتطبيقات",
            "الواقع الافتراضي والمعزز"
        ],
        tuition_fee=75000,
    ),
    "visual arts": College(
        name="كلية الفنون البصرية والتصميم",
        programs=["التصميم الداخلي والأثاث", "الإعلام والإعلان"],
        tuition_fee=60000,
    ),
    "business": College(
        name="كلية الأعمال والاقتصاد",
        programs=[
            "إدارة الأعمال والعلاقات الدولية",
            "الاقتصاد والتمويل الدولي",
            "المحاسبة والمعلوماتية الإدارية",
            "التسويق الرقمي والأعمال الإلكترونية",
            "التأمين والإحصاء"
        ],
        tuition_fee=50000,
    ),
    "energy": College(
        name="كلية علوم الطاقة",
        programs=["طاقة الوقود الأحفوري", "الطاقة المتجددة", "الطاقة النووية"],
        tuition_fee=45000,
    ),
}