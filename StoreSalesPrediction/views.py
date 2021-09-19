from django.shortcuts import render
import joblib
import numpy as np

def index(request):
    return render(request, 'index.html')



def prediction(request):
    return render(request, 'prediction.html')


def result(request):

    reg = joblib.load('model_final2.sav')
    inputs = []

    item_weight = float(request.POST['item_weight'])
    inputs.append(item_weight)


    item_visibility = float(request.POST['item_visibility'])
    inputs.append(item_visibility)


    item_mrp = float(request.POST['item_mrp'])
    inputs.append(item_mrp)


    outlet_establishment_year = int(request.POST['outlet_establishment_year'])
    inputs.append(outlet_establishment_year)


    item_fat_content = str(request.POST['item_fat_content'])
    if item_fat_content == 'Low Fat':
        item_fat_content_low_fat = 1
        item_fat_content_regular = 0
        inputs.append(item_fat_content_low_fat)
        inputs.append(item_fat_content_regular)
    elif item_fat_content == 'Regular':
        item_fat_content_low_fat = 0
        item_fat_content_regular = 1
        inputs.append(item_fat_content_low_fat)
        inputs.append(item_fat_content_regular)
    else:
        print("Error in Fat content")



    item_type = str(request.POST['item_type'])
   # Fruits and Vegetables, Snack, Foods, Household,Frozen Foods, Dairy, Canned, Baking,
   # Goods, Health and Hygiene, Soft, Drinks, Meat, Breads, Hard, Drinks,
   # Others, Starchy, Foods, Breakfast,Seafood
    if item_type == 'Fruits and Vegetables':
        item_type_fruits_and_vegetables =1
        item_type_snack_foods =0
        item_type_household =0
        item_type_frozen_foods =0
        item_type_dairy =0
        item_type_canned =0
        item_type_baking_goods =0
        item_type_health_and_hygiene =0
        item_type_soft_drinks =0
        item_type_meat =0
        item_type_breads =0
        item_type_hard_drinks =0
        item_type_others =0
        item_type_starchy_foods =0
        item_type_breakfast =0
        item_type_seafood =0
        inputs.append(item_type_fruits_and_vegetables)
        inputs.append(item_type_snack_foods)
        inputs.append(item_type_household)
        inputs.append(item_type_frozen_foods)
        inputs.append(item_type_dairy)
        inputs.append(item_type_canned)
        inputs.append(item_type_baking_goods)
        inputs.append(item_type_health_and_hygiene)
        inputs.append(item_type_soft_drinks)
        inputs.append(item_type_meat)
        inputs.append(item_type_breads)
        inputs.append(item_type_hard_drinks)
        inputs.append(item_type_others)
        inputs.append(item_type_starchy_foods)
        inputs.append(item_type_breakfast)
        inputs.append(item_type_seafood)
    elif item_type == 'Snack Foods':
        item_type_fruits_and_vegetables =0
        item_type_snack_foods =1
        item_type_household =0
        item_type_frozen_foods =0
        item_type_dairy =0
        item_type_canned =0
        item_type_baking_goods =0
        item_type_health_and_hygiene =0
        item_type_soft_drinks =0
        item_type_meat =0
        item_type_breads =0
        item_type_hard_drinks =0
        item_type_others =0
        item_type_starchy_foods =0
        item_type_breakfast =0
        item_type_seafood =0
        inputs.append(item_type_fruits_and_vegetables)
        inputs.append(item_type_snack_foods)
        inputs.append(item_type_household)
        inputs.append(item_type_frozen_foods)
        inputs.append(item_type_dairy)
        inputs.append(item_type_canned)
        inputs.append(item_type_baking_goods)
        inputs.append(item_type_health_and_hygiene)
        inputs.append(item_type_soft_drinks)
        inputs.append(item_type_meat)
        inputs.append(item_type_breads)
        inputs.append(item_type_hard_drinks)
        inputs.append(item_type_others)
        inputs.append(item_type_starchy_foods)
        inputs.append(item_type_breakfast)
        inputs.append(item_type_seafood)
    elif item_type == 'Household':
        item_type_fruits_and_vegetables =0
        item_type_snack_foods =0
        item_type_household =1
        item_type_frozen_foods =0
        item_type_dairy =0
        item_type_canned =0
        item_type_baking_goods =0
        item_type_health_and_hygiene =0
        item_type_soft_drinks =0
        item_type_meat =0
        item_type_breads =0
        item_type_hard_drinks =0
        item_type_others =0
        item_type_starchy_foods =0
        item_type_breakfast =0
        item_type_seafood =0
        inputs.append(item_type_fruits_and_vegetables)
        inputs.append(item_type_snack_foods)
        inputs.append(item_type_household)
        inputs.append(item_type_frozen_foods)
        inputs.append(item_type_dairy)
        inputs.append(item_type_canned)
        inputs.append(item_type_baking_goods)
        inputs.append(item_type_health_and_hygiene)
        inputs.append(item_type_soft_drinks)
        inputs.append(item_type_meat)
        inputs.append(item_type_breads)
        inputs.append(item_type_hard_drinks)
        inputs.append(item_type_others)
        inputs.append(item_type_starchy_foods)
        inputs.append(item_type_breakfast)
        inputs.append(item_type_seafood)
    elif item_type == 'Frozen Foods':
        item_type_fruits_and_vegetables =0
        item_type_snack_foods =0
        item_type_household =0
        item_type_frozen_foods =1
        item_type_dairy =0
        item_type_canned =0
        item_type_baking_goods =0
        item_type_health_and_hygiene =0
        item_type_soft_drinks =0
        item_type_meat =0
        item_type_breads =0
        item_type_hard_drinks =0
        item_type_others =0
        item_type_starchy_foods =0
        item_type_breakfast =0
        item_type_seafood =0
        inputs.append(item_type_fruits_and_vegetables)
        inputs.append(item_type_snack_foods)
        inputs.append(item_type_household)
        inputs.append(item_type_frozen_foods)
        inputs.append(item_type_dairy)
        inputs.append(item_type_canned)
        inputs.append(item_type_baking_goods)
        inputs.append(item_type_health_and_hygiene)
        inputs.append(item_type_soft_drinks)
        inputs.append(item_type_meat)
        inputs.append(item_type_breads)
        inputs.append(item_type_hard_drinks)
        inputs.append(item_type_others)
        inputs.append(item_type_starchy_foods)
        inputs.append(item_type_breakfast)
        inputs.append(item_type_seafood)
    elif item_type == 'Dairy':
        item_type_fruits_and_vegetables =0
        item_type_snack_foods =0
        item_type_household =0
        item_type_frozen_foods =0
        item_type_dairy =1
        item_type_canned =0
        item_type_baking_goods =0
        item_type_health_and_hygiene =0
        item_type_soft_drinks =0
        item_type_meat =0
        item_type_breads =0
        item_type_hard_drinks =0
        item_type_others =0
        item_type_starchy_foods =0
        item_type_breakfast =0
        item_type_seafood =0
        inputs.append(item_type_fruits_and_vegetables)
        inputs.append(item_type_snack_foods)
        inputs.append(item_type_household)
        inputs.append(item_type_frozen_foods)
        inputs.append(item_type_dairy)
        inputs.append(item_type_canned)
        inputs.append(item_type_baking_goods)
        inputs.append(item_type_health_and_hygiene)
        inputs.append(item_type_soft_drinks)
        inputs.append(item_type_meat)
        inputs.append(item_type_breads)
        inputs.append(item_type_hard_drinks)
        inputs.append(item_type_others)
        inputs.append(item_type_starchy_foods)
        inputs.append(item_type_breakfast)
        inputs.append(item_type_seafood)
    elif item_type == 'Canned':
        item_type_fruits_and_vegetables =0
        item_type_snack_foods =0
        item_type_household =0
        item_type_frozen_foods =0
        item_type_dairy =0
        item_type_canned =1
        item_type_baking_goods =0
        item_type_health_and_hygiene =0
        item_type_soft_drinks =0
        item_type_meat =0
        item_type_breads =0
        item_type_hard_drinks =0
        item_type_others =0
        item_type_starchy_foods =0
        item_type_breakfast =0
        item_type_seafood =0
        inputs.append(item_type_fruits_and_vegetables)
        inputs.append(item_type_snack_foods)
        inputs.append(item_type_household)
        inputs.append(item_type_frozen_foods)
        inputs.append(item_type_dairy)
        inputs.append(item_type_canned)
        inputs.append(item_type_baking_goods)
        inputs.append(item_type_health_and_hygiene)
        inputs.append(item_type_soft_drinks)
        inputs.append(item_type_meat)
        inputs.append(item_type_breads)
        inputs.append(item_type_hard_drinks)
        inputs.append(item_type_others)
        inputs.append(item_type_starchy_foods)
        inputs.append(item_type_breakfast)
        inputs.append(item_type_seafood)
    elif item_type == 'Baking Goods':
        item_type_fruits_and_vegetables =0
        item_type_snack_foods =0
        item_type_household =0
        item_type_frozen_foods =0
        item_type_dairy =0
        item_type_canned =0
        item_type_baking_goods =1
        item_type_health_and_hygiene =0
        item_type_soft_drinks =0
        item_type_meat =0
        item_type_breads =0
        item_type_hard_drinks =0
        item_type_others =0
        item_type_starchy_foods =0
        item_type_breakfast =0
        item_type_seafood =0
        inputs.append(item_type_fruits_and_vegetables)
        inputs.append(item_type_snack_foods)
        inputs.append(item_type_household)
        inputs.append(item_type_frozen_foods)
        inputs.append(item_type_dairy)
        inputs.append(item_type_canned)
        inputs.append(item_type_baking_goods)
        inputs.append(item_type_health_and_hygiene)
        inputs.append(item_type_soft_drinks)
        inputs.append(item_type_meat)
        inputs.append(item_type_breads)
        inputs.append(item_type_hard_drinks)
        inputs.append(item_type_others)
        inputs.append(item_type_starchy_foods)
        inputs.append(item_type_breakfast)
        inputs.append(item_type_seafood)
    elif item_type == 'Health and Hygiene':
        item_type_fruits_and_vegetables =0
        item_type_snack_foods =0
        item_type_household =0
        item_type_frozen_foods =0
        item_type_dairy =0
        item_type_canned =0
        item_type_baking_goods =0
        item_type_health_and_hygiene =1
        item_type_soft_drinks =0
        item_type_meat =0
        item_type_breads =0
        item_type_hard_drinks =0
        item_type_others =0
        item_type_starchy_foods =0
        item_type_breakfast =0
        item_type_seafood =0
        inputs.append(item_type_fruits_and_vegetables)
        inputs.append(item_type_snack_foods)
        inputs.append(item_type_household)
        inputs.append(item_type_frozen_foods)
        inputs.append(item_type_dairy)
        inputs.append(item_type_canned)
        inputs.append(item_type_baking_goods)
        inputs.append(item_type_health_and_hygiene)
        inputs.append(item_type_soft_drinks)
        inputs.append(item_type_meat)
        inputs.append(item_type_breads)
        inputs.append(item_type_hard_drinks)
        inputs.append(item_type_others)
        inputs.append(item_type_starchy_foods)
        inputs.append(item_type_breakfast)
        inputs.append(item_type_seafood)
    elif item_type == 'Soft Drinks':
        item_type_fruits_and_vegetables =0
        item_type_snack_foods =0
        item_type_household =0
        item_type_frozen_foods =0
        item_type_dairy =0
        item_type_canned =0
        item_type_baking_goods =0
        item_type_health_and_hygiene =0
        item_type_soft_drinks =1
        item_type_meat =0
        item_type_breads =0
        item_type_hard_drinks =0
        item_type_others =0
        item_type_starchy_foods =0
        item_type_breakfast =0
        item_type_seafood =0
        inputs.append(item_type_fruits_and_vegetables)
        inputs.append(item_type_snack_foods)
        inputs.append(item_type_household)
        inputs.append(item_type_frozen_foods)
        inputs.append(item_type_dairy)
        inputs.append(item_type_canned)
        inputs.append(item_type_baking_goods)
        inputs.append(item_type_health_and_hygiene)
        inputs.append(item_type_soft_drinks)
        inputs.append(item_type_meat)
        inputs.append(item_type_breads)
        inputs.append(item_type_hard_drinks)
        inputs.append(item_type_others)
        inputs.append(item_type_starchy_foods)
        inputs.append(item_type_breakfast)
        inputs.append(item_type_seafood)
    elif item_type == 'Meat':
        item_type_fruits_and_vegetables =0
        item_type_snack_foods =0
        item_type_household =0
        item_type_frozen_foods =0
        item_type_dairy =0
        item_type_canned =0
        item_type_baking_goods =0
        item_type_health_and_hygiene =0
        item_type_soft_drinks =0
        item_type_meat =1
        item_type_breads =0
        item_type_hard_drinks =0
        item_type_others =0
        item_type_starchy_foods =0
        item_type_breakfast =0
        item_type_seafood =0
        inputs.append(item_type_fruits_and_vegetables)
        inputs.append(item_type_snack_foods)
        inputs.append(item_type_household)
        inputs.append(item_type_frozen_foods)
        inputs.append(item_type_dairy)
        inputs.append(item_type_canned)
        inputs.append(item_type_baking_goods)
        inputs.append(item_type_health_and_hygiene)
        inputs.append(item_type_soft_drinks)
        inputs.append(item_type_meat)
        inputs.append(item_type_breads)
        inputs.append(item_type_hard_drinks)
        inputs.append(item_type_others)
        inputs.append(item_type_starchy_foods)
        inputs.append(item_type_breakfast)
        inputs.append(item_type_seafood)
    elif item_type == 'Breads':
        item_type_fruits_and_vegetables =0
        item_type_snack_foods =0
        item_type_household =0
        item_type_frozen_foods =0
        item_type_dairy =0
        item_type_canned =0
        item_type_baking_goods =0
        item_type_health_and_hygiene =0
        item_type_soft_drinks =0
        item_type_meat =0
        item_type_breads =1
        item_type_hard_drinks =0
        item_type_others =0
        item_type_starchy_foods =0
        item_type_breakfast =0
        item_type_seafood =0
        inputs.append(item_type_fruits_and_vegetables)
        inputs.append(item_type_snack_foods)
        inputs.append(item_type_household)
        inputs.append(item_type_frozen_foods)
        inputs.append(item_type_dairy)
        inputs.append(item_type_canned)
        inputs.append(item_type_baking_goods)
        inputs.append(item_type_health_and_hygiene)
        inputs.append(item_type_soft_drinks)
        inputs.append(item_type_meat)
        inputs.append(item_type_breads)
        inputs.append(item_type_hard_drinks)
        inputs.append(item_type_others)
        inputs.append(item_type_starchy_foods)
        inputs.append(item_type_breakfast)
        inputs.append(item_type_seafood)
    elif item_type == 'Hard drinks':
        item_type_fruits_and_vegetables =0
        item_type_snack_foods =0
        item_type_household =0
        item_type_frozen_foods =0
        item_type_dairy =0
        item_type_canned =0
        item_type_baking_goods =0
        item_type_health_and_hygiene =0
        item_type_soft_drinks =0
        item_type_meat =0
        item_type_breads =0
        item_type_hard_drinks =1
        item_type_others =0
        item_type_starchy_foods =0
        item_type_breakfast =0
        item_type_seafood =0
        inputs.append(item_type_fruits_and_vegetables)
        inputs.append(item_type_snack_foods)
        inputs.append(item_type_household)
        inputs.append(item_type_frozen_foods)
        inputs.append(item_type_dairy)
        inputs.append(item_type_canned)
        inputs.append(item_type_baking_goods)
        inputs.append(item_type_health_and_hygiene)
        inputs.append(item_type_soft_drinks)
        inputs.append(item_type_meat)
        inputs.append(item_type_breads)
        inputs.append(item_type_hard_drinks)
        inputs.append(item_type_others)
        inputs.append(item_type_starchy_foods)
        inputs.append(item_type_breakfast)
        inputs.append(item_type_seafood)
    elif item_type == 'Others':
        item_type_fruits_and_vegetables =0
        item_type_snack_foods =0
        item_type_household =0
        item_type_frozen_foods =0
        item_type_dairy =0
        item_type_canned =0
        item_type_baking_goods =0
        item_type_health_and_hygiene =0
        item_type_soft_drinks =0
        item_type_meat =0
        item_type_breads =0
        item_type_hard_drinks =0
        item_type_others =1
        item_type_starchy_foods =0
        item_type_breakfast =0
        item_type_seafood =0
        inputs.append(item_type_fruits_and_vegetables)
        inputs.append(item_type_snack_foods)
        inputs.append(item_type_household)
        inputs.append(item_type_frozen_foods)
        inputs.append(item_type_dairy)
        inputs.append(item_type_canned)
        inputs.append(item_type_baking_goods)
        inputs.append(item_type_health_and_hygiene)
        inputs.append(item_type_soft_drinks)
        inputs.append(item_type_meat)
        inputs.append(item_type_breads)
        inputs.append(item_type_hard_drinks)
        inputs.append(item_type_others)
        inputs.append(item_type_starchy_foods)
        inputs.append(item_type_breakfast)
        inputs.append(item_type_seafood)
    elif item_type == 'Starchy Foods':
        item_type_fruits_and_vegetables =0
        item_type_snack_foods =0
        item_type_household =0
        item_type_frozen_foods =0
        item_type_dairy =0
        item_type_canned =0
        item_type_baking_goods =0
        item_type_health_and_hygiene =0
        item_type_soft_drinks =0
        item_type_meat =0
        item_type_breads =0
        item_type_hard_drinks =0
        item_type_others =0
        item_type_starchy_foods =1
        item_type_breakfast =0
        item_type_seafood =0
        inputs.append(item_type_fruits_and_vegetables)
        inputs.append(item_type_snack_foods)
        inputs.append(item_type_household)
        inputs.append(item_type_frozen_foods)
        inputs.append(item_type_dairy)
        inputs.append(item_type_canned)
        inputs.append(item_type_baking_goods)
        inputs.append(item_type_health_and_hygiene)
        inputs.append(item_type_soft_drinks)
        inputs.append(item_type_meat)
        inputs.append(item_type_breads)
        inputs.append(item_type_hard_drinks)
        inputs.append(item_type_others)
        inputs.append(item_type_starchy_foods)
        inputs.append(item_type_breakfast)
        inputs.append(item_type_seafood)
    elif item_type == 'Breakfast':
        item_type_fruits_and_vegetables =0
        item_type_snack_foods =0
        item_type_household =0
        item_type_frozen_foods =0
        item_type_dairy =0
        item_type_canned =0
        item_type_baking_goods =0
        item_type_health_and_hygiene =0
        item_type_soft_drinks =0
        item_type_meat =0
        item_type_breads =0
        item_type_hard_drinks =0
        item_type_others =0
        item_type_starchy_foods =0
        item_type_breakfast =1
        item_type_seafood =0
        inputs.append(item_type_fruits_and_vegetables)
        inputs.append(item_type_snack_foods)
        inputs.append(item_type_household)
        inputs.append(item_type_frozen_foods)
        inputs.append(item_type_dairy)
        inputs.append(item_type_canned)
        inputs.append(item_type_baking_goods)
        inputs.append(item_type_health_and_hygiene)
        inputs.append(item_type_soft_drinks)
        inputs.append(item_type_meat)
        inputs.append(item_type_breads)
        inputs.append(item_type_hard_drinks)
        inputs.append(item_type_others)
        inputs.append(item_type_starchy_foods)
        inputs.append(item_type_breakfast)
        inputs.append(item_type_seafood)
    elif item_type == 'Seafood':
        item_type_fruits_and_vegetables =0
        item_type_snack_foods =0
        item_type_household =0
        item_type_frozen_foods =0
        item_type_dairy =0
        item_type_canned =0
        item_type_baking_goods =0
        item_type_health_and_hygiene =0
        item_type_soft_drinks =0
        item_type_meat =0
        item_type_breads =0
        item_type_hard_drinks =0
        item_type_others =0
        item_type_starchy_foods =0
        item_type_breakfast =0
        item_type_seafood =1
        inputs.append(item_type_fruits_and_vegetables)
        inputs.append(item_type_snack_foods)
        inputs.append(item_type_household)
        inputs.append(item_type_frozen_foods)
        inputs.append(item_type_dairy)
        inputs.append(item_type_canned)
        inputs.append(item_type_baking_goods)
        inputs.append(item_type_health_and_hygiene)
        inputs.append(item_type_soft_drinks)
        inputs.append(item_type_meat)
        inputs.append(item_type_breads)
        inputs.append(item_type_hard_drinks)
        inputs.append(item_type_others)
        inputs.append(item_type_starchy_foods)
        inputs.append(item_type_breakfast)
        inputs.append(item_type_seafood)
    else:
        print("error in item type")


    outlet_size= str(request.POST['outlet_size'])
    if outlet_size == 'Small':
        outlet_size_small=1
        outlet_size_medium=0
        outlet_size_high=0
        inputs.append(outlet_size_small)
        inputs.append(outlet_size_medium)
        inputs.append(outlet_size_high)
    elif outlet_size == 'Medium':
        outlet_size_small = 0
        outlet_size_medium = 1
        outlet_size_high = 0
        inputs.append(outlet_size_small)
        inputs.append(outlet_size_medium)
        inputs.append(outlet_size_high)
    elif outlet_size == 'High':
        outlet_size_small = 0
        outlet_size_medium = 0
        outlet_size_high = 1
        inputs.append(outlet_size_small)
        inputs.append(outlet_size_medium)
        inputs.append(outlet_size_high)
    else :
        print("error in outlet size")


    outlet_location_type = str(request.POST['outlet_location_type'])
    if outlet_location_type == 'Tier 1':
        outlet_location_type_tier_1= 1
        outlet_location_type_tier_2 = 0
        outlet_location_type_tier_3 = 0
        inputs.append(outlet_location_type_tier_1)
        inputs.append(outlet_location_type_tier_2)
        inputs.append(outlet_location_type_tier_3)
    elif outlet_location_type == 'Tier 2':
        outlet_location_type_tier_1 = 0
        outlet_location_type_tier_2 = 1
        outlet_location_type_tier_3 = 0
        inputs.append(outlet_location_type_tier_1)
        inputs.append(outlet_location_type_tier_2)
        inputs.append(outlet_location_type_tier_3)
    elif outlet_location_type == 'Tier 3':
        outlet_location_type_tier_1 = 0
        outlet_location_type_tier_2 = 0
        outlet_location_type_tier_3 = 1
        inputs.append(outlet_location_type_tier_1)
        inputs.append(outlet_location_type_tier_2)
        inputs.append(outlet_location_type_tier_3)
    else :
        print('error in outlet location type')

    outlet_type = str(request.POST['outlet_type'])
    if outlet_type == 'Grocery Store':
        outlet_type_grocery_store = 1
        outlet_type_supermarket_type1 = 0
        outlet_type_supermarket_type2=0
        outlet_type_supermarket_type3=0
        inputs.append(outlet_type_grocery_store)
        inputs.append(outlet_type_supermarket_type1)
        inputs.append(outlet_type_supermarket_type2)
        inputs.append(outlet_type_supermarket_type3)
    elif outlet_type == 'Supermarket Type1':
        outlet_type_grocery_store=0
        outlet_type_supermarket_type1=1
        outlet_type_supermarket_type2=0
        outlet_type_supermarket_type3=0
        inputs.append(outlet_type_grocery_store)
        inputs.append(outlet_type_supermarket_type1)
        inputs.append(outlet_type_supermarket_type2)
        inputs.append(outlet_type_supermarket_type3)
    elif outlet_type == 'Supermarket Type2':
        outlet_type_grocery_store = 0
        outlet_type_supermarket_type1 = 0
        outlet_type_supermarket_type2 = 1
        outlet_type_supermarket_type3 = 0
        inputs.append(outlet_type_grocery_store)
        inputs.append(outlet_type_supermarket_type1)
        inputs.append(outlet_type_supermarket_type2)
        inputs.append(outlet_type_supermarket_type3)
    elif outlet_type == 'Supermarket Type3':
        outlet_type_grocery_store = 0
        outlet_type_supermarket_type1 = 0
        outlet_type_supermarket_type2 = 0
        outlet_type_supermarket_type3 = 1
        inputs.append(outlet_type_grocery_store)
        inputs.append(outlet_type_supermarket_type1)
        inputs.append(outlet_type_supermarket_type2)
        inputs.append(outlet_type_supermarket_type3)
    else:
        print("error in outlet type")




    ans = reg.predict([inputs])
    pred = ans.flatten()
    pred=round(pred[0], 3)





    return render(request, 'result.html', {'pred':pred})