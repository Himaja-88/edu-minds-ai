import datetime

class StudyPlanner:
    def __init__(self, subjects, study_hours, available_hours_per_day):
        self.subjects = subjects
        self.study_hours = study_hours
        self.available_hours_per_day = available_hours_per_day
        self.study_plan = {}

    def generate_plan(self):
        total_hours_needed = sum(self.study_hours)
        days_needed = total_hours_needed // self.available_hours_per_day + (1 if total_hours_needed % self.available_hours_per_day != 0 else 0)

        # Generate a basic study schedule
        start_date = datetime.datetime.now()
        current_day = start_date
        hours_allocated = 0

        for day in range(days_needed):
            current_day_schedule = {}
            for i, subject in enumerate(self.subjects):
                if self.study_hours[i] > 0:
                    study_time = min(self.study_hours[i], self.available_hours_per_day)
                    self.study_hours[i] -= study_time
                    current_day_schedule[subject] = study_time
                    hours_allocated += study_time

            # Adding the day's schedule to the plan
            self.study_plan[current_day.strftime("%Y-%m-%d")] = current_day_schedule
            current_day += datetime.timedelta(days=1)

            if hours_allocated >= total_hours_needed:
                break

    def print_plan(self):
        print("\nYour Study Plan:")
        for date, plan in self.study_plan.items():
            print(f"\n{date}:")
            for subject, hours in plan.items():
                print(f"  - Study {subject} for {hours} hours")

# Example usage
subjects = ["Math", "History", "Science", "English"]
study_hours = [20, 15, 10, 5]  # Number of hours to study for each subject
available_hours_per_day = 5  # Available study time per day

planner = StudyPlanner(subjects, study_hours, available_hours_per_day)
planner.generate_plan()
planner.print_plan()
