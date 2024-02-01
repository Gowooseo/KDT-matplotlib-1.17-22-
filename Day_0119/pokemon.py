import requests
import pandas as pd
cookies = {
    '_cc_id': 'bd8f9ae87042a1e23999ec30664f5238',
    'panoramaId_expiry': '1706177996621',
    'panoramaId': 'bf0998fdce68ec739109ea9f3db4185ca02c166da0a92dccaaad0384aeb006a2',
    'panoramaIdType': 'panoDevice',
    '_au_1d': 'AU1D-0100-001705573198-O8ENXIII-JW4S',
    '_ga': 'GA1.2.1292711165.1705573199',
    '_gid': 'GA1.2.4163251.1705573199',
    '_au_last_seen_pixels': 'eyJhcG4iOjE3MDU2MzE1MTQsInR0ZCI6MTcwNTYzMTUxNCwicHViIjoxNzA1NjMxNTE0LCJydWIiOjE3MDU2MzE1MTQsInRhcGFkIjoxNzA1NjMxNTE0LCJhZHgiOjE3MDU2MzE1MTQsImdvbyI6MTcwNTYzMTUxNCwic21hcnQiOjE3MDU2MzE1MTQsImFkbyI6MTcwNTYzMTU0MywicHBudCI6MTcwNTYzMTY0MCwiYmVlcyI6MTcwNTYzMTU0MywiY29sb3NzdXMiOjE3MDU2MzE1NDMsImluZGV4IjoxNzA1NjMxNTQzLCJpbXByIjoxNzA1NjMxNTQzLCJ0YWJvb2xhIjoxNzA1NjMxNTQzLCJvcGVueCI6MTcwNTYzMTU0MywiYW1vIjoxNzA1NjMxNTQzLCJzb24iOjE3MDU2MzE1MTQsInVucnVseSI6MTcwNTYzMTU0M30%3D',
    '__gads': 'ID=bdce228b7b8a7e34:T=1705573198:RT=1705635005:S=ALNI_MZXR50btczIJF-1sfe06chwAdIdZQ',
    '__gpi': 'UID=00000cea72878a1d:T=1705635005:RT=1705635005:S=ALNI_MZye0rFYkjB793iHL5Ucg2H48MWkA',
    'cto_bundle': 'AJaFs194VkJpRkVkeTN3NGxocUpyWk56Y24lMkZ4WjFNNlRVSTBmRFVOSDBDdXhaNm1vRXdxdXBHYnhaUVMwVGU0UWhGMHRsJTJGdSUyRkZ3d2F2SnV0Z0FvTHFZU3B2bG1ZSVowOVFiUW8lMkJwemNlJTJGbm5uQkEzclBhT2R4JTJGaU91VnRrMm5zS3RPZWFkcTBIeDdzRVRzJTJCa0NjVTVIVzFEZyUzRCUzRA',
}

headers = {
    'authority': 'pokemondb.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ko,en;q=0.9,en-US;q=0.8',
    'cache-control': 'no-cache',
    # 'cookie': '_cc_id=bd8f9ae87042a1e23999ec30664f5238; panoramaId_expiry=1706177996621; panoramaId=bf0998fdce68ec739109ea9f3db4185ca02c166da0a92dccaaad0384aeb006a2; panoramaIdType=panoDevice; _au_1d=AU1D-0100-001705573198-O8ENXIII-JW4S; _ga=GA1.2.1292711165.1705573199; _gid=GA1.2.4163251.1705573199; _au_last_seen_pixels=eyJhcG4iOjE3MDU2MzE1MTQsInR0ZCI6MTcwNTYzMTUxNCwicHViIjoxNzA1NjMxNTE0LCJydWIiOjE3MDU2MzE1MTQsInRhcGFkIjoxNzA1NjMxNTE0LCJhZHgiOjE3MDU2MzE1MTQsImdvbyI6MTcwNTYzMTUxNCwic21hcnQiOjE3MDU2MzE1MTQsImFkbyI6MTcwNTYzMTU0MywicHBudCI6MTcwNTYzMTY0MCwiYmVlcyI6MTcwNTYzMTU0MywiY29sb3NzdXMiOjE3MDU2MzE1NDMsImluZGV4IjoxNzA1NjMxNTQzLCJpbXByIjoxNzA1NjMxNTQzLCJ0YWJvb2xhIjoxNzA1NjMxNTQzLCJvcGVueCI6MTcwNTYzMTU0MywiYW1vIjoxNzA1NjMxNTQzLCJzb24iOjE3MDU2MzE1MTQsInVucnVseSI6MTcwNTYzMTU0M30%3D; __gads=ID=bdce228b7b8a7e34:T=1705573198:RT=1705635005:S=ALNI_MZXR50btczIJF-1sfe06chwAdIdZQ; __gpi=UID=00000cea72878a1d:T=1705635005:RT=1705635005:S=ALNI_MZye0rFYkjB793iHL5Ucg2H48MWkA; cto_bundle=AJaFs194VkJpRkVkeTN3NGxocUpyWk56Y24lMkZ4WjFNNlRVSTBmRFVOSDBDdXhaNm1vRXdxdXBHYnhaUVMwVGU0UWhGMHRsJTJGdSUyRkZ3d2F2SnV0Z0FvTHFZU3B2bG1ZSVowOVFiUW8lMkJwemNlJTJGbm5uQkEzclBhT2R4JTJGaU91VnRrMm5zS3RPZWFkcTBIeDdzRVRzJTJCa0NjVTVIVzFEZyUzRCUzRA',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
}
response = requests.get('https://pokemondb.net/pokedex/all', cookies=cookies, headers=headers)

# print(response.text)

pokemondataText=response.text

pokemondataDF=pd.read_html(pokemondataText)[0]

print(type(pokemondataDF))

pokemondataDF.to_csv('pokemondata.csv')
