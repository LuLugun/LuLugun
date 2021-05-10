while True:  # 設立while無限迴圈
    try:  # try偵測錯誤
        a=exec(input(">>"))  # 將輸入值用eval函數執行
        print (a)  # 輸出結果
    except SyntaxError:  # 若遇到語法錯誤 輸出"invalid syntax"
        print ("invalid syntax")
    except:  # 若遇到錯誤 輸出"Error"
        print ("Error")
