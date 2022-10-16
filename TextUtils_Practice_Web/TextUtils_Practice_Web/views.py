# I am creating my first website in Django
from django.http import HttpResponse
from django.shortcuts import render


# Learned Urls and views.py handling in first video
# def index(request):
#   return HttpResponse("<H1> Hello My Name Is Soubhik Acharya </H1>")


# def about(request):
#   return HttpResponse("<H3> Hello My Name Is Soubhik Acharya, I am currently studying in Techno International New "
#                        "Town, "
#                        "I live in Dhanbad</H3>")


# def skills(request):
#  return HttpResponse("<H4> I know Programming Languages like c++, java, python and c </H4>")


# def MySocialAccounts(request):
#   return HttpResponse(
#         '''<H4> FB Account Link Click This to View My Account </H4><a href =
#         https://www.facebook.com/soubhik.acharya.1/"> @_@ Click And Visit On This Link @_@ </a>''')

def index(request):
    # parameters = {'Name': 'Soubhik Acharya', 'Place': 'Dhanbad'}
    # return HttpResponse("Home Page")

    return render(request, "index_3.html")


def analyze(request):
    Text_id_punc = request.POST.get('texteditor', 'default')
    # Check the CheckBox Values
    remove_punctuation = request.POST.get('remove_punc', 'off')
    full_caps = request.POST.get('fullcaps', 'off')
    new_line_remover = request.POST.get('newlineremover', 'off')
    extra_space_remover = request.POST.get('extraspaceremover', 'off')
    character_count = request.POST.get('charactercount', 'off')
    # print(full_caps)
    # print(remove_punctuation)
    # print(Text_id_punc)
    # If The value is On

    #
    if remove_punctuation == "on":
        # analyze = Text_id_punc
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyze = ""
        for char in Text_id_punc:
            if char not in punctuations:
                analyze = analyze + char
        parameters = {'purpose': "Removing Punctuations", 'analyzed_text': analyze}
        Text_id_punc = analyze
        # return render(request, 'analyze_2.html', parameters)

    if full_caps == "on":
        analyze = ""
        for char in Text_id_punc:
            analyze = analyze + char.upper()
        parameters = {'purpose': "Converted To Upper Case", 'analyzed_text': analyze}
        Text_id_punc = analyze
        # return render(request, 'analyze_2.html', parameters)

    if new_line_remover == "on":
        analyze = ""
        for char in Text_id_punc:
            if char != "\n" and char!= "\r":
                analyze = analyze + char
        parameters = {'purpose': "Removing the New Lines", 'analyzed_text': analyze}
        Text_id_punc = analyze
        # return render(request, 'analyze_2.html', parameters)

    if extra_space_remover == "on":
        analyze = ""
        for index, char in enumerate(Text_id_punc):
            # We can also use not after if .....
            if Text_id_punc[index] == " " and Text_id_punc[index + 1] == " ":
                pass
            else:
                analyze = analyze + char
        parameters = {'purpose': "Removing The Spaces", 'analyzed_text': analyze}
        Text_id_punc = analyze
        # return render(request, 'analyze_2.html', parameters)
# Here we are performing character count in our website
# Number of characters present in the text will be counted
    if character_count == "on":
        analyze = ('No. of characters given in the text are : '+str(len(Text_id_punc)))
        parameters = {'purpose': "Counting the number of character", 'analyzed_text': analyze}
        Text_id_punc = analyze
        # return render(request, 'analyze_2.html', parameters)
    if (remove_punctuation != "on" and full_caps != "on" and new_line_remover != "on" and extra_space_remover != "on" and character_count != "on"):
        return HttpResponse('''
           <div class="alert alert-info alert-dismissible fade show" role="alert">
              <strong>ERROR ! </strong> please select any operation and try again.
           </div>
        ''')




    # else:
    #     return HttpResponse("Shoot There is an Unexpected Error 404 !!!")
    return render(request, 'analyze_2.html', parameters)
# def analysis(request):
#     text = request.GET.get('texteditor', 'default')
#     print(text)
#     remove = request.GET.get('remove_punc', 'default')
#     print(remove)
#     if remove == 'on':
#         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#         analysis = ""
#         for char in text:
#             if char not in punctuations:
#                 analysis = analysis + char
#         params = {'purpose': 'Remove all', 'analyzed_text': analysis}
#         return render(request, 'analyze.html', params)
#     else:
#         return HttpResponse("Error ! Please Check the check box")


# def capitalization(request):
#     return HttpResponse("Capitalization First ")
#
#
# def newlineremover(request):
#     return HttpResponse("NewLine Remover between the characters <a href = '/'> Back </a>")
#
#
# def spaceremover(request):
#     return HttpResponse("Space Remover between the characters")
#
#
# def charcount(request):
#     return HttpResponse("The Number Of Character Counted")
