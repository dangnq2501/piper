import requests

textToSpeak = "Hiểu rõ ưu điểm và hạn chế của mỗi kiến trúc sẽ giúp bạn đưa ra quyết định phù hợp cho bài toán của mình. Mạng CNN Đa Nhánh là một kiến trúc trong đó mô hình được chia thành nhiều nhánh song song, mỗi nhánh có thể xử lý dữ liệu theo cách riêng, chẳng hạn như tập trung vào các dải tần số, đặc trưng không gian hoặc thời gian khác nhau của tín hiệu EEG. Mục tiêu là khai thác đồng thời nhiều khía cạnh của dữ liệu để cải thiện hiệu suất phân loại."
urlPiper = "http://localhost:5000"
outputFilename = "output.wav"

payload = {'text': textToSpeak}

r = requests.get(urlPiper,params=payload)

with open(outputFilename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)