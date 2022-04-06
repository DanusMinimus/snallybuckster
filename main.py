import grayhat as gh
import search_unique as su
import json
import argparse
import logging

def main():
    logging.basicConfig(format='[%(levelname)s]%(message)s', level=logging.INFO)

    parser = argparse.ArgumentParser(description="SnallyBuckster tool for locating unique files within buckets")
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')

    required.add_argument("-apik", type=str, help="API Key for Grayhatwarfare", required=True)
    required.add_argument("-bid", type=int, default=1, help="Bucket ID for querying", required=True)
    optional.add_argument("-pl", type=int, default=1000, help="Page limit for each query")

    args = parser.parse_args()

    token = args.apik
    b_id = args.bid
    limit_page = args.pl

    print(r"""\

        SnanllyBuckster - By Danus Minimus

                    \****__            ____                                              
                    |    *****\_      --/ *\-__                                          
                    /_          (_    ./ ,/----'                                         
            Art by     \__         (_./  /                                                
            Ironwing     \__           \___----^__                                       
                        _/   _                     \                                      
                    |    _/  __/ )\"\ _____         ***\_                                    
                    |\__/   /    ^ ^       \____          )                                   
                    \___--"                    \_________)                                  
                                                    """)

    gray_object = gh.Build(token)

    page = 0
    total_results = 1

    while page < total_results:
        query = gray_object.Buckets(bucket_id=b_id, start_page=page, stop_page=limit_page)
        s3_object = gh.s3(query)
        json_files = s3_object.perform_query()

        if total_results == 1:
            total_results = s3_object.get_total_results()

        for items in json_files['files']:
            su.search_files(items['url'])
        
        if page + limit_page > total_results:
            total_left = total_results - (page + limit_page)
            limit_page = limit_page + total_left

        page = page + limit_page

    logging.info("Total items parsed: %d\nDumping raw json data to data.json!", page)
    with open('data.json', 'w+', encoding='utf-8') as file_object:
        json.dump(json_files, file_object, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()





