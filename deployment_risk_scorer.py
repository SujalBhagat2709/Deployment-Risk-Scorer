"""
Deployment Risk Scorer
----------------------
File : deployment_risk_scorer.py

Purpose
-------
Estimates deployment risk before releasing a software change.

Features
--------
✔ Add Deployment
✔ Calculate Risk Score
✔ Risk Level
✔ Deployment Recommendation
✔ Risk Factors
✔ Deployment Report
✔ Summary
"""


class DeploymentRiskScorer:

    def __init__(self):

        self.deployments = []

    # ----------------------------------
    # Calculate Risk Score
    # ----------------------------------
    def calculate_risk(self,
                       changed_files,
                       test_coverage,
                       open_bugs,
                       previous_failures):

        score = 0

        # More changed files = higher risk
        if changed_files > 50:

            score += 30

        elif changed_files > 20:

            score += 20

        elif changed_files > 10:

            score += 10

        # Lower test coverage = higher risk
        if test_coverage < 60:

            score += 30

        elif test_coverage < 80:

            score += 20

        elif test_coverage < 90:

            score += 10

        # Open bugs
        if open_bugs >= 10:

            score += 25

        elif open_bugs >= 5:

            score += 15

        elif open_bugs > 0:

            score += 5

        # Previous deployment failures
        if previous_failures >= 5:

            score += 15

        elif previous_failures >= 2:

            score += 10

        elif previous_failures == 1:

            score += 5

        return min(score, 100)

    # ----------------------------------
    # Risk Level
    # ----------------------------------
    def risk_level(self,
                   score):

        if score >= 70:

            return "High"

        elif score >= 40:

            return "Medium"

        return "Low"

    # ----------------------------------
    # Deployment Recommendation
    # ----------------------------------
    def recommendation(self,
                       score):

        if score >= 70:

            return "Do Not Deploy"

        elif score >= 40:

            return "Review Before Deploying"

        return "Safe to Deploy"

    # ----------------------------------
    # Detect Risk Factors
    # ----------------------------------
    def risk_factors(self,
                     changed_files,
                     test_coverage,
                     open_bugs,
                     previous_failures):

        factors = []

        if changed_files > 20:

            factors.append(
                "Large number of changed files"
            )

        if test_coverage < 80:

            factors.append(
                "Low test coverage"
            )

        if open_bugs > 0:

            factors.append(
                "Open bugs present"
            )

        if previous_failures > 0:

            factors.append(
                "Previous deployment failures"
            )

        if not factors:

            factors.append(
                "No major risk factors detected"
            )

        return factors

    # ----------------------------------
    # Add Deployment
    # ----------------------------------
    def add_deployment(self,
                       deployment_id,
                       version,
                       changed_files,
                       test_coverage,
                       open_bugs,
                       previous_failures):

        risk_score = self.calculate_risk(

            changed_files,
            test_coverage,
            open_bugs,
            previous_failures

        )

        deployment = {

            "Deployment ID":
                deployment_id,

            "Version":
                version,

            "Changed Files":
                changed_files,

            "Test Coverage %":
                test_coverage,

            "Open Bugs":
                open_bugs,

            "Previous Failures":
                previous_failures,

            "Risk Score":
                risk_score,

            "Risk Level":
                self.risk_level(
                    risk_score
                ),

            "Recommendation":
                self.recommendation(
                    risk_score
                ),

            "Risk Factors":
                self.risk_factors(

                    changed_files,
                    test_coverage,
                    open_bugs,
                    previous_failures

                )

        }

        self.deployments.append(
            deployment
        )

        return deployment

    # ----------------------------------
    # Highest Risk Deployment
    # ----------------------------------
    def highest_risk(self):

        if not self.deployments:

            return None

        return max(

            self.deployments,

            key=lambda deployment:
            deployment["Risk Score"]

        )

    # ----------------------------------
    # Summary
    # ----------------------------------
    def summary(self):

        high = 0
        medium = 0
        low = 0

        for deployment in self.deployments:

            level = deployment["Risk Level"]

            if level == "High":

                high += 1

            elif level == "Medium":

                medium += 1

            else:

                low += 1

        return {

            "Total Deployments":
                len(self.deployments),

            "High Risk":
                high,

            "Medium Risk":
                medium,

            "Low Risk":
                low

        }

    # ----------------------------------
    # Display Deployment
    # ----------------------------------
    def display_deployment(self,
                           deployment):

        print(
            "\n========== DEPLOYMENT RISK ==========\n"
        )

        for key, value in deployment.items():

            print(
                f"{key:<22}: {value}"
            )

    # ----------------------------------
    # Display All Deployments
    # ----------------------------------
    def display_deployments(self):

        if not self.deployments:

            print(
                "\nNo deployment records available."
            )

            return

        print(
            "\n========== DEPLOYMENT REPORT ==========\n"
        )

        for deployment in self.deployments:

            print(
                f"{deployment['Deployment ID']} | "
                f"{deployment['Version']} | "
                f"{deployment['Risk Level']} | "
                f"Score: {deployment['Risk Score']}"
            )

    # ----------------------------------
    # Display Summary
    # ----------------------------------
    def display_summary(self):

        report = self.summary()

        print(
            "\n========== SUMMARY ==========\n"
        )

        for key, value in report.items():

            print(
                f"{key:<20}: {value}"
            )


# ----------------------------------
# Example
# ----------------------------------

if __name__ == "__main__":

    scorer = DeploymentRiskScorer()

    while True:

        print("\n1. Add Deployment")
        print("2. View Deployments")
        print("3. Highest Risk Deployment")
        print("4. Summary")
        print("5. Exit")

        choice = input(
            "\nEnter Choice: "
        )

        if choice == "1":

            deployment = scorer.add_deployment(

                input("Deployment ID: "),

                input("Version: "),

                int(
                    input(
                        "Changed Files: "
                    )
                ),

                float(
                    input(
                        "Test Coverage (%): "
                    )
                ),

                int(
                    input(
                        "Open Bugs: "
                    )
                ),

                int(
                    input(
                        "Previous Deployment Failures: "
                    )
                )

            )

            scorer.display_deployment(
                deployment
            )

        elif choice == "2":

            scorer.display_deployments()

        elif choice == "3":

            deployment = scorer.highest_risk()

            if deployment:

                scorer.display_deployment(
                    deployment
                )

            else:

                print(
                    "\nNo deployments available."
                )

        elif choice == "4":

            scorer.display_summary()

        elif choice == "5":

            print(
                "\nThank you for using Deployment Risk Scorer."
            )

            break

        else:

            print(
                "\nInvalid choice."
            )