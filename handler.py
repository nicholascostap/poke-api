def is_valid_response(status_code: int) -> bool | str:
    try:
        match status_code:
            case 200:
                return True
            case 204:
                return "No Content"
            case 400:
                raise Exception("Bad Request")
            case 404:
                raise Exception("Not Found")
            case 500:
                raise Exception("Internal Server Error")
            case 502:
                raise Exception("Bad Gateway")
            case _:
                raise Exception("Unknown")
    
    except Exception as exc:
        print(exc)
        return False
