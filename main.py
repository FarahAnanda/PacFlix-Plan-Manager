# import library
from tabulate import tabulate

#create data
data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}

#create User class
class User:
    def __init__(self, username):
        self.username = username
    
    #checking benefits of each plan
    def check_benefit(self):
        #init headers
        headers = ["Basic Plan", "Standard Plan", "Premium Plan"]
        
        #init table
        table = [[True, True, True, "Stream Available"],
                 [True, True, True, "Download Available"],
                 [True, True, True, "SD Quality"],
                 [False, True, True, "HD Quality"],
                 [False, False, True, "UHD Quality"],
                 [1, 2, 4, "Number of Devices"],
                 ["3rd party Movie only", "Basic Plan Content + Sports", "Basic Plan + Standard Plan + PacFlix Original Series", "Jenis Konten"],
                 [120_000, 160_000, 200_000, "Price"]]
        
        print("PacFlix Plan List")
        print("")
        print(tabulate(table, headers, tablefmt = "github"))
    
    #checking plan based on username
    def check_plan(self, username):
        #iterate keys and values based on date
        for key, value in data.items():
            #create branching
            if key == self.username:
                get_current_plan = value[0]
                get_duration_plan = value[1]
                
                print(f"Username: {self.username}")
                print(f"Current Plan: {get_current_plan}")
                print(f"Duration Plan: {get_duration_plan} months")
    
    # create upgrade plan method based on username
    def upgrade_plan(self, username, upgrade_plan):
        DISCOUNT = 0.05

        # Check if upgrade_plan and current_plan are valid options
        if upgrade_plan not in data or get_current_plan not in data:
            raise Exception("Plan not available.")

        # Get the index of the upgrade plan and current plan in the plan list
        plan_list = list(data.keys())
        upgrade_index = plan_list.index(upgrade_plan)
        current_index = plan_list.index(get_current_plan)

        # Check if the upgrade plan is higher than the current plan
        if upgrade_index <= current_index:
            raise Exception("You can only upgrade to a higher plan.")

        # Calculate total payment based on upgrade plan and discount
        if get_duration_plan > 12:
            total = data[upgrade_plan][-1] - (data[upgrade_plan][-1] * DISCOUNT)
        else:
            total = data[upgrade_plan][-1]
        return total

#create object for User class
user_1 = User(username = "Shandy")
user_2 = User(username = "Cahya")
user_3 = User(username = "Ana")
user_4 = User(username = "Bagus")

#create NewUser class
class NewUser:
    referral_code = []
    
    def __init__(self, username):
        self.username = username
        
    def get_referral_code(self, data):
        for value in data.values():
            ref_code = value[2]
            #append to empty list
            self.referral_code.append(ref_code)
            
        return self.referral_code
    
    def pick_plan(self, new_plan, referral_code):
        DISCOUNT = 0.04
        
        if referral_code in self.referral_code:
            if new_plan == "Basic Plan":
                total = 120_000 - (120_000 * DISCOUNT)
                return total
            
            elif new_plan == "Standard Plan":
                total = 160_000 - (160_000 * DISCOUNT)
                return total
            
            elif new_plan == "Premium Plan":
                total = 200_000 - (200_000 * DISCOUNT)
                return total
            
            else:
                raise Exceptiton("Plan not available.")
        
        else:
            raise Exception("Referral code not available.")

#create object for NewUser class
faizal = NewUser("faizal_icikiwir")

#test case 1
user_3.check_benefit()

#test case 2
user_1.check_plan(user_1.username)

#test case 3
user_2.upgrade_plan(username = user_2.username,
                   upgrade_plan = "Premium Plan")

#test case 4
faizal.get_referral_code(data = data)
faizal.pick_plan(new_plan = "Basic Plan",
                referral_code = "bagus-9f92")

#testing with another object
user_2.check_benefit()
user_3.check_plan(user_3.username)
user_1.upgrade_plan(username = user_1.username,
                   upgrade_plan = "Standard Plan")
faizal.pick_plan("Basic Plan", "indira-22gs")
