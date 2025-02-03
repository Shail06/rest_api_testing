import os
import subprocess

if __name__ == "__main__":
    test_reports_dir = "./test-report"
    if not (os.path.exists(test_reports_dir)):
        os.makedirs(test_reports_dir)
    subprocess.run(["python3","-m","behave", "features/", "-f", "html", "-o", os.path.join(test_reports_dir, "report.html")])
