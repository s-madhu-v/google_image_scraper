import sys
from serpapi import GoogleSearch

#API_KEY = "812b89e5b4f99b9bc964df84895a910b715c04955629eb247637c9361026865e"
API_KEY = sys.argv[1]
images_per_term = 200

params = {
  "q": "overflow",
  "tbm": "isch",
  "ijn": "0",
  "api_key": API_KEY
}

def get_links(parameters, number_of_images):
    n = int(number_of_images/100)
    links = []
    for i in range(n):
        try:
            search = GoogleSearch(parameters)
            results = search.get_dict()
            images_results = results["images_results"]
            image_links = [x["original"] for x in images_results]
            links = links + image_links
            parameters["ijn"] = str(int(parameters["ijn"]) + 1)
        except KeyError:
            break
    return links

def write_to_file(filename, parameters, n):
    with open(filename, 'w') as fp:
        for item in get_links(parameters, n):
            fp.write("%s\n" % item)
    print("=================================================================")
    print(f"File Done: {filename}")
    print("=================================================================")

def search_terms():
    terms = [sys.argv[2]]
    for x in terms:
        params["q"] = x
        f = "image-links/" + x + ".txt"
        write_to_file(f, params, images_per_term)

search_terms()