while read line; do
    python3 scrape.py 812b89e5b4f99b9bc964df84895a910b715c04955629eb247637c9361026865e "$line"
done < search_terms.txt