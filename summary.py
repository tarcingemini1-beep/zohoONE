import pandas as pd
df = pd.read_csv('psg_hod_database.csv')

print("## Verification Summary")
print(f"Total target departments requested: {len(df)}")
verified = df[df['Verification Status'] == 'Verified']
unverified = df[df['Verification Status'] == 'Unverified']
print(f"Verified standalone departments with mapped HODs: {len(verified)}")
print(f"Unverified/Programs (Standalone dept does not exist): {len(unverified)}")

print("\n## Unresolved/Ambiguous Departments (Not Standalone)")
for i, r in unverified.iterrows():
    print(f"- {r['Department']}: {r['Notes']}")

print("\n## Source URLs Used")
print("- Homepage: https://psgtech.edu/")
print("- Programmes Listing: https://psgtech.edu/programme_offered.php")
print("- Official Departments Hub: https://psgtech.edu/index.php")
print("- Official Heads Directory: https://psgtech.edu/Heads.php")
print("- Official Contacts: https://psgtech.edu/cont.php")
