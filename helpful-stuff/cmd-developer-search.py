def normal_search(site_name, site_domain, query):
    if query != "":
        import webbrowser
        import time
        custom_website_search = f"https://www.{site_name}.{site_domain}/search?q={query}/"
        print(f"\nYour search query has been saved and processed opening in {site_name}")
        time.sleep(3)
        webbrowser.open(custom_website_search)
    else:
        print("Sorry search must have a value")


def custom_search(site_name, site_domain, query_structure, query):
    if query != "":
        import webbrowser
        import time
        custom_website_search = f"https://www.{site_name}.{site_domain}/{query_structure}={query}"
        print(f"\nYour search query has been saved and processed opening in {site_name}")
        time.sleep(3)
        webbrowser.open(custom_website_search)

question = input("Does the site use the normal structure of search queries ['www.example.com/search?q=your_query']$ |-> ")


if question == "yes" or question == "y":
    website_name = input("What is the site name ... |> ")  # Name of website
    website_domain = input("What is the site domain ... [e.g -> com, org, net, io] |> ")  # Website domain
    search_query = input(f"What do you want to search on {website_name}: ")  # Search query

    """ Neccessary parameters for the normal_search() function, don't touch them or it might brake! """
    normal_search(website_name, website_domain, search_query)


elif question == "no" or question == "n":

    website_link = input("Please provide a sample of a website search query -> ")  # Sample to be debug for the new search query link
    import re

    different_1 = re.compile("/?[a-zA-Z]=")  # Expression for `example.com/?q=your-query`

    """ TODO: Find a solution to the regex pattern ... """
    different_2 = re.compile("/[a-zA-Z]?[A-Za-z]=")  # Expression for `example.com/namesearch?=blahblahblah`

    search_pattern = different_1.search(website_link)  # Search `website_link` for the expression

    """ TODO: Make the `search_pattern_2` and the `elif` function work also ... """
    search_pattern_2 = different_2.search(website_link)  # Search `website_link` for the expression

    if search_pattern:
        # Grabs the website-name from the website-link/website-url
        website_name = website_link.split(".")
        grabbed_website_name = website_name[0]
        formatted_website_name = grabbed_website_name.upper()

        # Grabs the website-domain from the website-link/website-url
        website_domain = website_link.split(".")
        grabbed_website_domain = website_domain[1]
        if grabbed_website_domain.find("/"):
            splitting = grabbed_website_domain.split("/")
            new_grabbed_website_domain = splitting[0]

            final_website_domain = new_grabbed_website_domain

        # Grabs the website-query-structure from the website-link/website-url
        website_search_query_structure = website_link.split("/")
        grabbed_website_search_query_structure_step_1 = website_search_query_structure[1]
        grabbed_website_search_query_structure_step_2 = grabbed_website_search_query_structure_step_1.split("=")
        grabbed_website_search_query_structure_final_step = grabbed_website_search_query_structure_step_2[0]

        search_query = input(f"What do you want to search on {formatted_website_name.lower()}: ")  # Ask for input for the search query

        """ Neccessary parameters for the custom_search() function, don't touch them or it might brake! """
        custom_search(formatted_website_name, final_website_domain, grabbed_website_search_query_structure_final_step, search_query)

    elif search_pattern_2:
        website_name = website_link.split(".")
        grabbed_website_name = website_name[1]
        formatted_website_name = grabbed_website_name.upper()

        print(formatted_website_name)


"""

---------------
Important Notes
---------------
This file is highly unstable so don't edit it if you don't know what your doing

Made by LokotamaTheMastermind
@created_at -> 8/26/2020
@email -> lokotamathemastermind2@gmail.com

---------------
"""
