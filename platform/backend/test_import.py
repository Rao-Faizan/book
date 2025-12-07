print("Starting import...")
try:
    from app.main import app
    print("Import successful!")
except Exception as e:
    print(f"Import failed: {e}")
print("End of script")
