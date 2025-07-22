import requests

def read_data() -> str:
    response = requests.get("https://gist.githubusercontent.com/cradiator/7fc01879115f993446ad9aa67859204b/raw/57de7d4fbd4f5069e2cff6c0fd2da314b98fe968/%25E5%2585%25B3%25E4%25BA%258E%25E4%25BB%25A4%25E7%258B%2590%25E5%2586%25B2%25E8%25BD%25AC%25E7%2594%259F%25E4%25B8%25BA%25E5%258F%25B2%25E8%258E%25B1%25E5%25A7%2586%25E5%25B9%25B6%25E5%25AF%25B9%25E4%25B8%2596%25E7%2595%258C%25E7%258C%25AE%25E4%25B8%258A%25E4%25BA%2586%25E7%25BE%258E%25E5%25A5%25BD%25E7%259A%2584%25E7%2582%258E%25E7%2588%2586%25E8%25BF%2599%25E4%25BB%25B6%25E4%25BA%258B.txt")
    return response.text

def get_chunks() -> list[str]:
    content = read_data()
    chunks = content.split('\n\n')
    
    result = []
    header = ""
    for c in chunks:
        if c.startswith("#"):
            header += f"{c}\n"
        else:
            result.append(f"{header}{c}")
            header = ""

    return result

if __name__ == '__main__':
    chunks = get_chunks()
    for c in chunks:
        print(c)
        print("--------------")