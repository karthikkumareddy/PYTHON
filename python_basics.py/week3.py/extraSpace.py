s = "   Hello   World   "

# ముందు, చివర స్పేస్‌లు మాత్రమే తీసేయడానికి:
print(s.strip())             # Output: "Hello   World"

# మధ్యలో ఉన్న ఎక్స్‌ట్రా స్పేస్‌లు కూడా తీసేయడానికి (Best way):
clean = " ".join(s.split())
print(clean)                 # Output: "Hello World"
