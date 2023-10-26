from django.http.response import HttpResponse
from django.http.request import HttpRequest


def near_hundred_view(request: HttpRequest, number: int) -> HttpResponse:
    isNear = (abs(100 - number) <= 10) or (abs(200 - number) <= 10)
    return HttpResponse(isNear)


def string_splosion_view(request: HttpRequest, word: str) -> HttpResponse:
    newWord = ""

    for charPos in range(0, len(word)):
        newWord += word[:charPos]

    return HttpResponse(newWord + word)


def cat_dog_view(request: HttpRequest, phrase: str) -> HttpResponse:
    cat_count = 0
    dog_count = 0

    for charPos in range(0, len(phrase) - 1):  # wow
        if phrase[charPos] == "c":  # this was such a good way to do this...
            if phrase[charPos + 1] == "a":
                if phrase[charPos + 2] == "t":
                    cat_count += 1

        if phrase[charPos] == "d":
            if phrase[charPos + 1] == "o":
                if phrase[charPos + 2] == "g":
                    dog_count += 1

    return HttpResponse(cat_count == dog_count)


def lone_sum_view(
    request: HttpRequest, first: int, second: int, third: int
) -> HttpResponse:
    numbList = [first, second, third]
    total = 0

    for numb in numbList:
        if not numbList.count(numb) > 1:
            total += numb

    return HttpResponse(total)
