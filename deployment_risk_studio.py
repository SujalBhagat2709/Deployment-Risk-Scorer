"""
Deployment Risk Studio
----------------------
Main interface for Deployment Risk Scorer.
"""

from deployment_risk_scorer import DeploymentRiskScorer


class DeploymentRiskStudio:

    def __init__(self):

        self.scorer = DeploymentRiskScorer()

    # ----------------------------------
    # Add Deployment
    # ----------------------------------
    def add_deployment(self):

        print(
            "\n========== ADD DEPLOYMENT ==========\n"
        )

        deployment_id = input(
            "Deployment ID: "
        ).strip()

        version = input(
            "Version: "
        ).strip()

        changed_files = int(
            input(
                "Changed Files: "
            )
        )

        test_coverage = float(
            input(
                "Test Coverage (%): "
            )
        )

        open_bugs = int(
            input(
                "Open Bugs: "
            )
        )

        previous_failures = int(
            input(
                "Previous Deployment Failures: "
            )
        )

        deployment = self.scorer.add_deployment(

            deployment_id,
            version,
            changed_files,
            test_coverage,
            open_bugs,
            previous_failures

        )

        print(
            "\nDeployment risk calculated successfully."
        )

        self.scorer.display_deployment(
            deployment
        )

    # ----------------------------------
    # View Deployments
    # ----------------------------------
    def view_deployments(self):

        self.scorer.display_deployments()

    # ----------------------------------
    # Highest Risk
    # ----------------------------------
    def highest_risk(self):

        deployment = self.scorer.highest_risk()

        if deployment:

            print(
                "\n========== HIGHEST RISK DEPLOYMENT ==========\n"
            )

            self.scorer.display_deployment(
                deployment
            )

        else:

            print(
                "\nNo deployments available."
            )

    # ----------------------------------
    # Summary
    # ----------------------------------
    def summary(self):

        self.scorer.display_summary()

    # ----------------------------------
    # Menu
    # ----------------------------------
    def menu(self):

        while True:

            print("\n" + "=" * 60)
            print("          DEPLOYMENT RISK SCORER")
            print("=" * 60)

            print("1. Add Deployment")
            print("2. View Deployments")
            print("3. Highest Risk Deployment")
            print("4. Summary")
            print("5. Exit")

            choice = input(
                "\nEnter Choice: "
            ).strip()

            if choice == "1":

                self.add_deployment()

            elif choice == "2":

                self.view_deployments()

            elif choice == "3":

                self.highest_risk()

            elif choice == "4":

                self.summary()

            elif choice == "5":

                print(
                    "\nThank you for using Deployment Risk Scorer."
                )

                break

            else:

                print(
                    "\nInvalid choice."
                )


# ----------------------------------
# Main
# ----------------------------------

if __name__ == "__main__":

    studio = DeploymentRiskStudio()

    studio.menu()