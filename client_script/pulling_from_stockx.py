import pandas as pd
import os
import sys
import time
import random
from random import randint
import requests
import csv
import smtplib
import string
import random
import math
from datetime import datetime
from app.models import Input

from client_script import shopify_api as sapi
# import shopify_api as sapi

from client_script.user_agent_lists import user_agent_master_list

# - Need to handle error handling, and headers.

round_up = math.ceil

# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# Setting pandas viewing
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
pd.set_option("display.max_rows", None)
pd.options.mode.chained_assignment = None

# Setting base dir
basedir = os.path.dirname(sys.argv[0])

condition_list = ["DS", "LW", "MW", "HW", "RB", "BG", "SS", "SLW", "SW", "SH"]

# -----------------------------------THIS IS WHERE FRONT END WILL CONNECT THE VARIABLES FOR CONDITIONS-----------------------------------------

input1 = Input.query.filter(Input.name == "value1").first()
input2 = Input.query.filter(Input.name == "value2").first()
input3 = Input.query.filter(Input.name == "value3").first()
input4 = Input.query.filter(Input.name == "value4").first()
input5 = Input.query.filter(Input.name == "value5").first()
input6 = Input.query.filter(Input.name == "value6").first()
input7 = Input.query.filter(Input.name == "value7").first()
input8 = Input.query.filter(Input.name == "value8").first()
input9 = Input.query.filter(Input.name == "value9").first()
input10 = Input.query.filter(Input.name == "value10").first()

# Added
DS_condition = input1.value
print("Your deadstock pricing variable is set to:", DS_condition)

# Added
SDS_condition = input2.value
print("Your special deadstock pricing variable is set to:", SDS_condition)

# Multiply
LW_condition = input3.value
print("Your lightly worn pricing variable is set to:", LW_condition)

# Multiply
MW_condition = input4.value
print("Your moderately worn pricing variable is set to:", MW_condition)

# Multiply
HW_condition = input5.value
print("Your heavily worn pricing variable is set to:", HW_condition)

# Multiply
RB_condition = input6.value
print("Your replacement box pricing variable is set to:", RB_condition)

# Multiply
BG_condition = input7.value
print("Your b-grade pricing variable is set to:", BG_condition)

# Multiply
SLW_condition = input8.value
print("Your special lightly worn pricing variable is set to:", SLW_condition)

# Multiply
SMW_condition = input9.value
print("Your heavily special moderately worn variable is set to:", SMW_condition)

# Multiply
SHW_condition = input10.value
print("Your special heavily worn pricing variable is set to:", SHW_condition)

# -----------------------------------THIS IS WHERE FRONT END WILL CONNECT THE VARIABLES FOR CONDITIONS-----------------------------------------


user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko)"

print("Your user agent is set to:", user_agent)

base = 5

headers = {"User-Agent": user_agent}

all_items_from_shopify = []

current_items_from_shopify = []
# Use this to understand the page layout of the shopify products.
skus = []
# Use this to reference dictionary by SKU, and associated product link page
sku_url_dictionary = {}

sku_website_info_dict = {}
sku_website_list = []

all_sizes_list = []

logged_in = 0

user_agent_counter = 0

stockx_url_api = "https://stockx.com/api/browse?&_search="

product_title_and_image_dict = {}
title_and_image_list = []

product_size_and_price_dict = {}

final_dict = {}
final_list = []
number_of_products_total = 1

counter = 0

header_counter = 0

pause_counter = 0

over_32_variants = []


def checking_variables(multiplier):
    if multiplier > 1.0:
        print(
            "You entered",
            multiplier,
            ". This is a whole number instead of a decimal. Please change this and re-run the program.",
        )


def initiate_check():
    checking_variables(LW_condition)
    checking_variables(MW_condition)
    checking_variables(HW_condition)
    checking_variables(RB_condition)
    checking_variables(BG_condition)
    checking_variables(SLW_condition)
    checking_variables(SMW_condition)
    checking_variables(SHW_condition)


def inventory():
    global inventory_by_id_dict
    inventory_by_id_dict = sapi.iterate_through_json()
    return inventory_by_id_dict


def breaking_sku_down():
    inventory_by_id_dict = inventory()
    for key, value in inventory_by_id_dict.items():
        variant_sku = key
        inv_id = value[0]
        image = value = [1]
        # Splitting items from SKU list to get each individual variable
        try:
            item_split = variant_sku.split("/")
            sku = item_split[0]
            #  print(sku)

            second_half = item_split[1]
            #     print(second_half)
            print("SKU", sku)
            print("SIZE AND CONDITION", second_half)
            second_half_split = second_half.split("|")
            #  print(second_half_split)
            size_and_condition = second_half_split[0]
            condition = [ele for ele in condition_list if (ele in size_and_condition)]
            condition = str(condition)
            #   print(condition)
            condition = condition.replace("[", "")
            condition = condition.replace("]", "")
            condition = condition.replace("'", "")
            size = size_and_condition.replace(condition, "")
            #    print(size)
            # Add all items from the cell to a list
            current_items_from_shopify.append(sku)
            current_items_from_shopify.append(size)
            current_items_from_shopify.append(condition)
            # Make a copy of the list so you can clear the original, and it doesn't delete data from list.
            appended_list = current_items_from_shopify[:]
            # Add that list to a master list
            all_items_from_shopify.append(appended_list)
            # Clear the list for the next
            current_items_from_shopify.clear()
            print(" ")
        #   print(condition)
        #   print(size)
        except Exception as e:
            #  print(e)
            sku = variant_sku
            #  print(e)
            print("SKU ", sku, "cannot be separated because no '/' is present.")
            size = "N/A"
            condition = "N/A"
            # Add all items from the cell to a list
            current_items_from_shopify.append(sku)
            current_items_from_shopify.append(size)
            current_items_from_shopify.append(condition)
            # Make a copy of the list so you can clear the original, and it doesn't delete data from list.
            appended_list = current_items_from_shopify[:]
            # Add that list to a master list
            all_items_from_shopify.append(appended_list)
            # Clear the list for the next
            current_items_from_shopify.clear()
            print(" ")


def loop_through_list():
    # Iterate through shopify sku row that's now in a list. Calling in base product function to separate duplicates, and add individuals to a dictionary
    for item in all_items_from_shopify:
        sku = item[0]
        size = item[1]
        condition = item[2]
        base_product_link_to_list(sku)
        print(sku)


# adding individual skus to a dictionary, with website base link.
def base_product_link_to_list(sku):
    global logged_in
    if sku in sku_url_dictionary:
        # appending it to the list, so we can keep track of the number of items in the csv. The dictionary in the "else" will be used to reference back to the URL, and the link to it.
        skus.append(sku)
    #     print(sku, ' already present')
    else:
        product_url = stockx_url_api + sku
        skus.append(sku)
        sku_url_dictionary[sku] = product_url
    logged_in += 1


def loop_through_base_product_link():
    for sku in sku_url_dictionary:
        link = sku_url_dictionary[sku]
        print("Updating info on sku...", sku)
        rotate_headers_if_needed(sku, link)


def rotate_headers_if_needed(sku, link):
    global user_agent
    global header_counter
    global pause_counter
    time.sleep(randint(4, 12))
    response = requests.get(link, headers=headers)
    response.raise_for_status()  # raise exception if invalid response
    shoe_data = response.json()
    getting_product_info(shoe_data, sku)
    user_agent_size = len(user_agent)
    if pause_counter == 45:
        print("Hit 45 SKUs - Pausing for 300-400 seconds")
        time.sleep(randint(300, 400))
    elif pause_counter == 100:
        print("Hit 100 SKUs - Pausing for 120-250 seconds")
        time.sleep(randint(120, 250))
    elif pause_counter == 134:
        print("Hit 134 SKUs - Pausing for 120-190 seconds")
        time.sleep(randint(120, 190))
    elif pause_counter == 200:
        print("Hit 200 SKUs - Pausing for 300-410 seconds")
        time.sleep(randint(300, 410))
    elif pause_counter == 260:
        print("Hit 260 SKUs - Pausing for 120-220 seconds")
        time.sleep(randint(120, 220))
    elif pause_counter == 320:
        print("Hit 320 SKUs - Pausing for 200-230 seconds")
        time.sleep(randint(200, 230))
    elif pause_counter == 440:
        print("Hit 440 SKUs - Pausing for 120-180 seconds")
        time.sleep(randint(120, 180))
    elif pause_counter == 550:
        print("Hit 550 SKUs - Pausing for 300-340 seconds")
        time.sleep(randint(300, 340))
    elif pause_counter == 640:
        print("Hit 640 SKUs - Pausing for 200-220 seconds")
        print("Resetting counter")
        time.sleep(randint(200, 220))
        pause_counter = 0
    if header_counter == 12:
        new_user_agent = user_agent[: user_agent_size - 8]
        letters = string.ascii_lowercase
        random_letter = "".join(random.choice(letters) for i in range(8))
        final_ua = new_user_agent + random_letter
        user_agent = final_ua
        header_counter = 0
        print(
            "-------------------------------USER AGENT ROTATED----------------------------------------"
        )
    header_counter += 1
    pause_counter += 1


# header_counter += 1


def getting_product_info(
    shoe_data, product_sku
):  # Pulling stockx data for real-time pricing, titles, and photos
    # clearing

    product_size_and_price_dict[
        product_sku
    ] = {}  # allows us to separate prices by size, attached to the singular SKU

    product_counter = 0

    try:
        # this will give you the amount of sizes offered for the product. Setting a for loop to iterate through each product to get the price, associated with the size, which will stop when the amount of sizes is reached
        shoe_size = shoe_data["Facets"]["shoeSize"]
        amount_of_sizes = len(shoe_size)
        #    print('Size ',shoe_size)
        #    print('Amount of sizes ', amount_of_sizes)
        # This is a deeper dive into the product itself. Now we can get the details such as image, shoe size, title, etc.
        product = shoe_data["Products"]
        #    print('Product ', product)
        # Not sure why we have to do this
        product_info = product[0]
        #   print('Product info ', product_info)

        # Getting the product image
        media = product_info["media"]
        product_image = media["imageUrl"]
        #   print('Media ', media)
        #   print('Product image ', product_image)
        #    print(product_image)

        # Getting the product title
        product_title = product_info["title"]
        #   print('Product title ', product_title)
        #    print(product_title)
        #    print('Number of sizes.. ', amount_of_sizes )
        #   print(title_and_image_list)

        title_and_image_list.append(product_title)
        title_and_image_list.append(product_image)
        copied_title_and_image = title_and_image_list[:]
        title_and_image_list.clear()
        product_title_and_image_dict[product_sku] = copied_title_and_image
        while product_counter <= amount_of_sizes:
            # Added this try statement within the while statement because stockX backend isn't matching up properly. Reporting the number of shoes present based off the front end, but back end only
            # accounting for a few of them, causing the bot to break.
            try:
                #   print(product_info)
                product_info = product[product_counter]
                product_market_pricing = product_info["market"]
                product_size_unsplit = product_info["market"]["lowestAskSize"]
                product_size_split = product_size_unsplit.split(",")
                product_size = product_size_split[0]
                product_price = product_info["market"]["lowestAsk"]
                #           print(product_price)
                product_size_and_price_dict[product_sku][product_size] = product_price
                #       Counting the sizes in each product, so we can pair the prices with the right size
                #        print(product_counter)
                product_counter += 1
            except Exception:
                product_counter += 1
                print(
                    '"Bid" possibly present. Only updating SKUs that have a price associated with them on StockX'
                )
                pass
    except Exception as e:
        product_title_and_image_dict[product_sku] = ["N/A", "N/A"]
        product_size_and_price_dict[product_sku]["0"] = ["0"]
        print(e)


def updating_everything():  # Creating new dictionaries based on information in the sheet, and the previous information in dictionaries from the stockx website
    global number_of_products_total
    for shoe in all_items_from_shopify:
        final_list.clear()
        sku = shoe[0]  # Getting sku size from shopify
        # print(sku)
        size = shoe[1]
        #  print(size)
        condition = shoe[2]
        updated_title_and_image = product_title_and_image_dict[sku]
        print(" ")
        print(
            "Looking in sheet at SKU number ..(",
            sku,
            "). Size ",
            size,
            "Found. Here are all listed sizes with prices that are on StockX:",
            product_size_and_price_dict[sku],
        )
        try:
            not_updated_price = product_size_and_price_dict[sku][size]
            print("not updated price", not_updated_price)
        except Exception:
            if "Y" in size:
                print(" ")
                print(
                    "WARNING:",
                    sku,
                    "is ",
                    size,
                    ". This size is not listed on stockx. Please see the following for the sizes listed on stockx: ",
                    product_size_and_price_dict[sku],
                )
                size_stripped = size.split("Y")
                new_size = size_stripped[0]
                print("--New size", new_size)
                try:
                    not_updated_price = product_size_and_price_dict[sku][new_size]
                    print("not updated price", not_updated_price)
                except Exception as e:
                    print(
                        "--Stripped the 'Y' out of SKU ",
                        sku,
                        "size ",
                        size,
                        ". The new size is ",
                        new_size,
                        " but it was still unable to be found on StockX. "
                        "Program will continue, but this price will not be updated.",
                    )
                    not_updated_price = 0
                    not_updated_price = int(not_updated_price)
            elif "W" in size:
                print(" ")
                print(
                    "WARNING:",
                    sku,
                    "is ",
                    size,
                    ". This size is not listed on stockx. Please see the following for the sizes listed on stockx: ",
                    product_size_and_price_dict[sku],
                )
                size_stripped = size.split("W")
                new_size = size_stripped[0]
                print("--New size", new_size)
                try:
                    not_updated_price = product_size_and_price_dict[sku][new_size]
                    print("not updated price", not_updated_price)
                except Exception as e:
                    print(
                        "--Stripped the 'W' out of SKU ",
                        sku,
                        "size ",
                        size,
                        ". The new size is ",
                        new_size,
                        " but it was still unable to be found on StockX. "
                        "Program will continue, but this price will not be updated.",
                    )
                    not_updated_price = 0
                    not_updated_price = int(not_updated_price)
            elif "C" in size:
                print(" ")
                print(
                    "WARNING:",
                    sku,
                    "is ",
                    size,
                    ". This size is not listed on stockx. Please see the following for the sizes listed on stockx: ",
                    product_size_and_price_dict[sku],
                )
                size_stripped = size.split("C")
                new_size = size_stripped[0]
                print("--New size", new_size)
                try:
                    not_updated_price = product_size_and_price_dict[sku][new_size]
                    print("not updated price", not_updated_price)
                except Exception as e:
                    print(
                        "--Stripped the 'C' out of SKU ",
                        sku,
                        "size ",
                        size,
                        ". The new size is ",
                        new_size,
                        " but it was still unable to be found on StockX. "
                        "Program will continue, but this price will not be updated.",
                    )
                    not_updated_price = 0
                    not_updated_price = int(not_updated_price)
            else:
                print("SKU ", sku, " couldnt be updated")
                not_updated_price = 0
                not_updated_price = int(not_updated_price)
        #        print('product title & image',updated_title_and_image) #matching that sku to dictionary containing updated information on title and image
        #       print('before price update',not_updated_price) #matching that sku to dictionary containing size by price for certain sku's
        #        print('condition',condition)
        if not_updated_price == 0:
            updated_price = 0
            print("product or size not on stockx")
        else:
            updated_price = condition_pricing(
                condition,
                not_updated_price,
                DS_condition,
                LW_condition,
                MW_condition,
                HW_condition,
                RB_condition,
                BG_condition,
                SDS_condition,
                SLW_condition,
                SMW_condition,
                SHW_condition,
            )
            print("updated price ", updated_price)

        final_dict[number_of_products_total] = [
            updated_title_and_image,
            updated_price,
            sku + "/" + size + condition,
        ]
        number_of_products_total += 1


#        print(number_of_products_total)


def send_to_shopify():
    global inventory_by_id_dict
    for key, value in final_dict.items():
        products_updated = key
        title = value[0][0]
        image = value[0][1]
        if "&updated_at" in image:
            image_split = image.split("&updated_at")
            new_image = image_split[0]
            image = new_image
        sku = value[2]
        updated_price = value[1]
        print("Sku: ", sku)
        print("Title: ", title)
        print("image:", image)
        print("updated_price: ", updated_price)
        if "N/A" in title:
            pass
        else:
            print("would uplaod")
            prod_id_list = inventory_by_id_dict[sku]
            prod_id = prod_id_list[2]
            v_id = prod_id_list[0]
            print("PROD_ID FROM STORE: ", prod_id)
            # All variants present in the store currently
            pull_from_shop = sapi.get_variant_count(prod_id)
            num_of_variants = pull_from_shop[0]
            single_v_ids = pull_from_shop[1]
            print("NUMBER OF VARIANTS UNDER THIS SKU: ", num_of_variants)
            print("CURRENT VARIANT: ", v_id)
            print("VARIANT IDS: ", single_v_ids)
            print("               ")

            sapi.update_shopify_store(
                prod_id,
                title,
                updated_price,
                image,
                num_of_variants,
                v_id,
                single_v_ids,
            )
            if num_of_variants >= 6:
                if sku.split("/")[0] in over_32_variants:
                    pass
                else:
                    over_32_variants.append(sku.split("/")[0])


def condition_pricing(
    condition,
    lowest_asking,
    DS_condition,
    LW_condition,
    MW_condition,
    HW_condition,
    RB_condition,
    BG_condition,
    SDS_condition,
    SLW_condition,
    SMW_condition,
    SHW_condition,
):  # To accurately price the products in the store based on the two input variables coming from text files

    if condition == "DS":
        price = (lowest_asking * 1.03) + 13.95 + DS_condition
        price = base * round_up(price / base)
        return price

    elif condition == "LW":
        price = (LW_condition * lowest_asking * 1.03) + 13.95
        price = base * round_up(price / base)
        return price

    elif condition == "MW":
        price = (MW_condition * lowest_asking * 1.03) + 13.95
        price = base * round_up(price / base)
        return price

    elif condition == "HW":
        price = (HW_condition * lowest_asking * 1.03) + 13.95
        price = base * round_up(price / base)
        return price

    elif condition == "RB":
        price = (RB_condition * lowest_asking * 1.03) + 13.95
        price = base * round_up(price / base)
        return price

    elif condition == "BG":
        price = (BG_condition * lowest_asking * 1.03) + 13.95
        price = base * round_up(price / base)
        return price

    elif condition == "SS":
        price = ((lowest_asking * 1.03) + 13.95) + SDS_condition
        price = base * round_up(price / base)
        return price

    elif condition == "SLW" or condition == "SL":
        #   price = (((lowest_asking * 1.03) + 13.95) + SDS_condition) * SLW_condition
        price = (SLW_condition * lowest_asking * 1.03) + 13.95
        price = base * round_up(price / base)
        return price

    elif condition == "SM":
        # price = (((lowest_asking * 1.03) + 13.95) + SDS_condition) * SMW_condition
        price = (SMW_condition * lowest_asking * 1.03) + 13.95
        price = base * round_up(price / base)
        return price

    elif condition == "SH":
        # price = (((lowest_asking * 1.03) + 13.95) + SDS_condition) * SHW_condition
        price = (SHW_condition * lowest_asking * 1.03) + 13.95
        price = base * round_up(price / base)
        return price


def all():
    global user_agent
    run_counter = 1
    run_successful = False

    while run_successful == False:
        if run_counter == 1:
            try:
                initiate_check()
                breaking_sku_down()
                loop_through_list()
                # try:
                loop_through_base_product_link()
                updating_everything()
                send_to_shopify()
                print(' ')
                print('updated')
                run_successful = True
                return run_successful
            except Exception as e:
                print(e)
                time.sleep(10)
                run_counter += 1
                user_agent = random.choice(user_agent_master_list)
                print("Fail number: ", str(run_counter))
                print('new useragent: ', user_agent)
        elif run_counter >1 and run_counter <= 10:
            try:
                loop_through_base_product_link()
                updating_everything()
                send_to_shopify()
                print(' ')
                print('updated')
                run_successful = True
                return run_successful
            except Exception as e:
                print(e)
                time.sleep(10)
                run_counter += 1
                user_agent = random.choice(user_agent_master_list)
                print("Fail number: ", str(run_counter))
                print('new useragent: ', user_agent)

if __name__ == "__main__":
    all()