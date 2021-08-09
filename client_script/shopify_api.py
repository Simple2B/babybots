import requests
from datetime import datetime


shopify_date = datetime.today().strftime("%Y-%m-%d")
split_date = shopify_date.split("-")
shopify_date_for_url = split_date[0] + "-" + split_date[1]
print(shopify_date_for_url)


# url = "https://42a4429bb4781c96e952b674904785f9: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@frontrunners-com.myshopify.com/admin/api/" + shopify_date_for_url + "/"

url = "https://42a4429bb4781c96e952b674904785f9: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@frontrunners-com.myshopify.com/admin/api/2021-07/"

# To get the list of products - GET
endpoint = "products.json"

# To update an existing product - PUT
pushing_product = "products/{}.json"

# To create a new product - POST
create_new_product = "products.json"


SKUs_from_shopify_by_id = {}
SKUs_from_shopify_by_sku = {}

# Getting products from shopify store
def get_products():
    r = requests.get(url + endpoint)
    return r.json()


# 6901649309863


def get_variant_count(prod_id):
    global num_of_variants
    products = get_products()
    product_list = products["products"]
    list_of_variants = []
    for product in product_list:
        # print(product['id'])
        product_id = product["id"]
        if product_id == int(prod_id):
            num_of_variants = len(product["variants"])
            # print(len(product['variants']))
            for variant in product["variants"]:
                single_v_id = variant["id"]
                # print(variant['id'])
                list_of_variants.append(single_v_id)
    return num_of_variants, list_of_variants


def iterate_through_json():
    global count
    # Getting product json file, and setting to list for iterating
    products = get_products()
    product_list = products["products"]  # Getting all products
    for product in product_list:  # Looping through products
        product_type = product["product_type"]  # Filtering by product type
        if product_type == "Shoes":  # Setting to shoe product type
            variants = product[
                "variants"
            ]  # Getting variant for matches. Each product variant has its own id, which we use to update shopify store.
            for variant in variants:
                product_id = variant["product_id"]
                id = variant["id"]
                sku = variant["sku"]
                image = variant["image_id"]
                #          SKUs_from_shopify_by_id[id] = [sku, image, product_id] #EXTRA - This is here incase we ever need to utilize the dict by prod ID in shopify. The way the script is configured, were matching by SKU.
                SKUs_from_shopify_by_sku[sku] = [id, image, product_id]
    return SKUs_from_shopify_by_sku


def update_shopify_store(prod_id, title, price, image, num_of_var, v_id, single_v_ids):
    global payload
    shopify_api = url + pushing_product.format(prod_id)

    single_v_ids.remove(v_id)
    if num_of_var == 1:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    }
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 2:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 3:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 4:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 5:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 6:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 7:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 8:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 9:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 10:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 11:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                    {
                        "id": single_v_ids[9],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 12:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                    {
                        "id": single_v_ids[9],
                    },
                    {
                        "id": single_v_ids[10],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 13:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                    {
                        "id": single_v_ids[9],
                    },
                    {
                        "id": single_v_ids[10],
                    },
                    {
                        "id": single_v_ids[11],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 14:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                    {
                        "id": single_v_ids[9],
                    },
                    {
                        "id": single_v_ids[10],
                    },
                    {
                        "id": single_v_ids[11],
                    },
                    {
                        "id": single_v_ids[12],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 15:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                    {
                        "id": single_v_ids[9],
                    },
                    {
                        "id": single_v_ids[10],
                    },
                    {
                        "id": single_v_ids[11],
                    },
                    {
                        "id": single_v_ids[12],
                    },
                    {
                        "id": single_v_ids[13],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 16:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                    {
                        "id": single_v_ids[9],
                    },
                    {
                        "id": single_v_ids[10],
                    },
                    {
                        "id": single_v_ids[11],
                    },
                    {
                        "id": single_v_ids[12],
                    },
                    {
                        "id": single_v_ids[13],
                    },
                    {
                        "id": single_v_ids[14],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 17:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                    {
                        "id": single_v_ids[9],
                    },
                    {
                        "id": single_v_ids[10],
                    },
                    {
                        "id": single_v_ids[11],
                    },
                    {
                        "id": single_v_ids[12],
                    },
                    {
                        "id": single_v_ids[13],
                    },
                    {
                        "id": single_v_ids[14],
                    },
                    {
                        "id": single_v_ids[15],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 18:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                    {
                        "id": single_v_ids[9],
                    },
                    {
                        "id": single_v_ids[10],
                    },
                    {
                        "id": single_v_ids[11],
                    },
                    {
                        "id": single_v_ids[12],
                    },
                    {
                        "id": single_v_ids[13],
                    },
                    {
                        "id": single_v_ids[14],
                    },
                    {
                        "id": single_v_ids[15],
                    },
                    {
                        "id": single_v_ids[16],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 19:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                    {
                        "id": single_v_ids[9],
                    },
                    {
                        "id": single_v_ids[10],
                    },
                    {
                        "id": single_v_ids[11],
                    },
                    {
                        "id": single_v_ids[12],
                    },
                    {
                        "id": single_v_ids[13],
                    },
                    {
                        "id": single_v_ids[14],
                    },
                    {
                        "id": single_v_ids[15],
                    },
                    {
                        "id": single_v_ids[16],
                    },
                    {
                        "id": single_v_ids[17],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 20:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                    {
                        "id": single_v_ids[9],
                    },
                    {
                        "id": single_v_ids[10],
                    },
                    {
                        "id": single_v_ids[11],
                    },
                    {
                        "id": single_v_ids[12],
                    },
                    {
                        "id": single_v_ids[13],
                    },
                    {
                        "id": single_v_ids[14],
                    },
                    {
                        "id": single_v_ids[15],
                    },
                    {
                        "id": single_v_ids[16],
                    },
                    {
                        "id": single_v_ids[17],
                    },
                    {
                        "id": single_v_ids[18],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 21:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                    {
                        "id": single_v_ids[9],
                    },
                    {
                        "id": single_v_ids[10],
                    },
                    {
                        "id": single_v_ids[11],
                    },
                    {
                        "id": single_v_ids[12],
                    },
                    {
                        "id": single_v_ids[13],
                    },
                    {
                        "id": single_v_ids[14],
                    },
                    {
                        "id": single_v_ids[15],
                    },
                    {
                        "id": single_v_ids[16],
                    },
                    {
                        "id": single_v_ids[17],
                    },
                    {
                        "id": single_v_ids[18],
                    },
                    {
                        "id": single_v_ids[19],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 22:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                    {
                        "id": single_v_ids[9],
                    },
                    {
                        "id": single_v_ids[10],
                    },
                    {
                        "id": single_v_ids[11],
                    },
                    {
                        "id": single_v_ids[12],
                    },
                    {
                        "id": single_v_ids[13],
                    },
                    {
                        "id": single_v_ids[14],
                    },
                    {
                        "id": single_v_ids[15],
                    },
                    {
                        "id": single_v_ids[16],
                    },
                    {
                        "id": single_v_ids[17],
                    },
                    {
                        "id": single_v_ids[18],
                    },
                    {
                        "id": single_v_ids[19],
                    },
                    {
                        "id": single_v_ids[20],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 23:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                    {
                        "id": single_v_ids[9],
                    },
                    {
                        "id": single_v_ids[10],
                    },
                    {
                        "id": single_v_ids[11],
                    },
                    {
                        "id": single_v_ids[12],
                    },
                    {
                        "id": single_v_ids[13],
                    },
                    {
                        "id": single_v_ids[14],
                    },
                    {
                        "id": single_v_ids[15],
                    },
                    {
                        "id": single_v_ids[16],
                    },
                    {
                        "id": single_v_ids[17],
                    },
                    {
                        "id": single_v_ids[18],
                    },
                    {
                        "id": single_v_ids[19],
                    },
                    {
                        "id": single_v_ids[20],
                    },
                    {
                        "id": single_v_ids[21],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 24:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                    {
                        "id": single_v_ids[9],
                    },
                    {
                        "id": single_v_ids[10],
                    },
                    {
                        "id": single_v_ids[11],
                    },
                    {
                        "id": single_v_ids[12],
                    },
                    {
                        "id": single_v_ids[13],
                    },
                    {
                        "id": single_v_ids[14],
                    },
                    {
                        "id": single_v_ids[15],
                    },
                    {
                        "id": single_v_ids[16],
                    },
                    {
                        "id": single_v_ids[17],
                    },
                    {
                        "id": single_v_ids[18],
                    },
                    {
                        "id": single_v_ids[19],
                    },
                    {
                        "id": single_v_ids[20],
                    },
                    {
                        "id": single_v_ids[21],
                    },
                    {
                        "id": single_v_ids[22],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 25:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                    {
                        "id": single_v_ids[9],
                    },
                    {
                        "id": single_v_ids[10],
                    },
                    {
                        "id": single_v_ids[11],
                    },
                    {
                        "id": single_v_ids[12],
                    },
                    {
                        "id": single_v_ids[13],
                    },
                    {
                        "id": single_v_ids[14],
                    },
                    {
                        "id": single_v_ids[15],
                    },
                    {
                        "id": single_v_ids[16],
                    },
                    {
                        "id": single_v_ids[17],
                    },
                    {
                        "id": single_v_ids[18],
                    },
                    {
                        "id": single_v_ids[19],
                    },
                    {
                        "id": single_v_ids[20],
                    },
                    {
                        "id": single_v_ids[21],
                    },
                    {
                        "id": single_v_ids[22],
                    },
                    {
                        "id": single_v_ids[23],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 26:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                    {
                        "id": single_v_ids[9],
                    },
                    {
                        "id": single_v_ids[10],
                    },
                    {
                        "id": single_v_ids[11],
                    },
                    {
                        "id": single_v_ids[12],
                    },
                    {
                        "id": single_v_ids[13],
                    },
                    {
                        "id": single_v_ids[14],
                    },
                    {
                        "id": single_v_ids[15],
                    },
                    {
                        "id": single_v_ids[16],
                    },
                    {
                        "id": single_v_ids[17],
                    },
                    {
                        "id": single_v_ids[18],
                    },
                    {
                        "id": single_v_ids[19],
                    },
                    {
                        "id": single_v_ids[20],
                    },
                    {
                        "id": single_v_ids[21],
                    },
                    {
                        "id": single_v_ids[22],
                    },
                    {
                        "id": single_v_ids[23],
                    },
                    {
                        "id": single_v_ids[24],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 27:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                    {
                        "id": single_v_ids[9],
                    },
                    {
                        "id": single_v_ids[10],
                    },
                    {
                        "id": single_v_ids[11],
                    },
                    {
                        "id": single_v_ids[12],
                    },
                    {
                        "id": single_v_ids[13],
                    },
                    {
                        "id": single_v_ids[14],
                    },
                    {
                        "id": single_v_ids[15],
                    },
                    {
                        "id": single_v_ids[16],
                    },
                    {
                        "id": single_v_ids[17],
                    },
                    {
                        "id": single_v_ids[18],
                    },
                    {
                        "id": single_v_ids[19],
                    },
                    {
                        "id": single_v_ids[20],
                    },
                    {
                        "id": single_v_ids[21],
                    },
                    {
                        "id": single_v_ids[22],
                    },
                    {
                        "id": single_v_ids[23],
                    },
                    {
                        "id": single_v_ids[24],
                    },
                    {
                        "id": single_v_ids[25],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 28:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                    {
                        "id": single_v_ids[9],
                    },
                    {
                        "id": single_v_ids[10],
                    },
                    {
                        "id": single_v_ids[11],
                    },
                    {
                        "id": single_v_ids[12],
                    },
                    {
                        "id": single_v_ids[13],
                    },
                    {
                        "id": single_v_ids[14],
                    },
                    {
                        "id": single_v_ids[15],
                    },
                    {
                        "id": single_v_ids[16],
                    },
                    {
                        "id": single_v_ids[17],
                    },
                    {
                        "id": single_v_ids[18],
                    },
                    {
                        "id": single_v_ids[19],
                    },
                    {
                        "id": single_v_ids[20],
                    },
                    {
                        "id": single_v_ids[21],
                    },
                    {
                        "id": single_v_ids[22],
                    },
                    {
                        "id": single_v_ids[23],
                    },
                    {
                        "id": single_v_ids[24],
                    },
                    {
                        "id": single_v_ids[25],
                    },
                    {
                        "id": single_v_ids[26],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 29:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                    {
                        "id": single_v_ids[9],
                    },
                    {
                        "id": single_v_ids[10],
                    },
                    {
                        "id": single_v_ids[11],
                    },
                    {
                        "id": single_v_ids[12],
                    },
                    {
                        "id": single_v_ids[13],
                    },
                    {
                        "id": single_v_ids[14],
                    },
                    {
                        "id": single_v_ids[15],
                    },
                    {
                        "id": single_v_ids[16],
                    },
                    {
                        "id": single_v_ids[17],
                    },
                    {
                        "id": single_v_ids[18],
                    },
                    {
                        "id": single_v_ids[19],
                    },
                    {
                        "id": single_v_ids[20],
                    },
                    {
                        "id": single_v_ids[21],
                    },
                    {
                        "id": single_v_ids[22],
                    },
                    {
                        "id": single_v_ids[23],
                    },
                    {
                        "id": single_v_ids[24],
                    },
                    {
                        "id": single_v_ids[25],
                    },
                    {
                        "id": single_v_ids[26],
                    },
                    {
                        "id": single_v_ids[27],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 30:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                    {
                        "id": single_v_ids[9],
                    },
                    {
                        "id": single_v_ids[10],
                    },
                    {
                        "id": single_v_ids[11],
                    },
                    {
                        "id": single_v_ids[12],
                    },
                    {
                        "id": single_v_ids[13],
                    },
                    {
                        "id": single_v_ids[14],
                    },
                    {
                        "id": single_v_ids[15],
                    },
                    {
                        "id": single_v_ids[16],
                    },
                    {
                        "id": single_v_ids[17],
                    },
                    {
                        "id": single_v_ids[18],
                    },
                    {
                        "id": single_v_ids[19],
                    },
                    {
                        "id": single_v_ids[20],
                    },
                    {
                        "id": single_v_ids[21],
                    },
                    {
                        "id": single_v_ids[22],
                    },
                    {
                        "id": single_v_ids[23],
                    },
                    {
                        "id": single_v_ids[24],
                    },
                    {
                        "id": single_v_ids[25],
                    },
                    {
                        "id": single_v_ids[26],
                    },
                    {
                        "id": single_v_ids[27],
                    },
                    {
                        "id": single_v_ids[28],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var == 31:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                    {
                        "id": single_v_ids[9],
                    },
                    {
                        "id": single_v_ids[10],
                    },
                    {
                        "id": single_v_ids[11],
                    },
                    {
                        "id": single_v_ids[12],
                    },
                    {
                        "id": single_v_ids[13],
                    },
                    {
                        "id": single_v_ids[14],
                    },
                    {
                        "id": single_v_ids[15],
                    },
                    {
                        "id": single_v_ids[16],
                    },
                    {
                        "id": single_v_ids[17],
                    },
                    {
                        "id": single_v_ids[18],
                    },
                    {
                        "id": single_v_ids[19],
                    },
                    {
                        "id": single_v_ids[20],
                    },
                    {
                        "id": single_v_ids[21],
                    },
                    {
                        "id": single_v_ids[22],
                    },
                    {
                        "id": single_v_ids[23],
                    },
                    {
                        "id": single_v_ids[24],
                    },
                    {
                        "id": single_v_ids[25],
                    },
                    {
                        "id": single_v_ids[26],
                    },
                    {
                        "id": single_v_ids[27],
                    },
                    {
                        "id": single_v_ids[28],
                    },
                    {
                        "id": single_v_ids[29],
                    },
                ],
                "images": [{"src": image}],
            }
        }
    elif num_of_var >= 32:
        payload = {
            "product": {
                "id": prod_id,
                "title": title,
                "variants": [
                    {
                        "id": v_id,
                        "price": price,
                    },
                    {
                        "id": single_v_ids[0],
                    },
                    {
                        "id": single_v_ids[1],
                    },
                    {
                        "id": single_v_ids[2],
                    },
                    {
                        "id": single_v_ids[3],
                    },
                    {
                        "id": single_v_ids[4],
                    },
                    {
                        "id": single_v_ids[5],
                    },
                    {
                        "id": single_v_ids[6],
                    },
                    {
                        "id": single_v_ids[7],
                    },
                    {
                        "id": single_v_ids[8],
                    },
                    {
                        "id": single_v_ids[9],
                    },
                    {
                        "id": single_v_ids[10],
                    },
                    {
                        "id": single_v_ids[11],
                    },
                    {
                        "id": single_v_ids[12],
                    },
                    {
                        "id": single_v_ids[13],
                    },
                    {
                        "id": single_v_ids[14],
                    },
                    {
                        "id": single_v_ids[15],
                    },
                    {
                        "id": single_v_ids[16],
                    },
                    {
                        "id": single_v_ids[17],
                    },
                    {
                        "id": single_v_ids[18],
                    },
                    {
                        "id": single_v_ids[19],
                    },
                    {
                        "id": single_v_ids[20],
                    },
                    {
                        "id": single_v_ids[21],
                    },
                    {
                        "id": single_v_ids[22],
                    },
                    {
                        "id": single_v_ids[23],
                    },
                    {
                        "id": single_v_ids[24],
                    },
                    {
                        "id": single_v_ids[25],
                    },
                    {
                        "id": single_v_ids[26],
                    },
                    {
                        "id": single_v_ids[27],
                    },
                    {
                        "id": single_v_ids[28],
                    },
                    {
                        "id": single_v_ids[29],
                    },
                    {
                        "id": single_v_ids[30],
                    },
                ],
                "images": [{"src": image}],
            }
        }

    r = requests.put(shopify_api, json=payload)
    print(r.json())
    return
