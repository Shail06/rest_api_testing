from utils.soft_assert import SoftAssert

def before_scenario(context, scenario):
    context.soft_assert = SoftAssert()
    
def after_scenario(context, scenario):
    pass
    