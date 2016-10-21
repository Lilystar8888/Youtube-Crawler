# Youtube Crawler 

/**
 * @file youtube.py
 * @author 0456155 
 * @brief A youtube crawler which extracts titles and descriptions of search results.
 * @date 2016/3/10
 * 請依照下列格式輸入指令：
 * python youtube.py [-h] [-n] [-p] keyword
 * -h     print help
 * -n     number of search result. default is 5
 * -p     page that you parse
 * --------------------------------------------------------------------------------------------
 * 系統預設n=5,p=1,若無"-n","-p"兩tags，則依據系統預設做Output.
 * Youtube contains at most 20 results in a page. And 50 pages at most for any search.
 * Therefore, n<=20, p<=50
 * 若系統回傳，Wrong Argument Input，請檢查Input是與依據輸入規格之順序。
 * 為維持Output排版，"-h"tag僅限單獨使用。ex: "python youtube.py -h -n 5 NA"系統將回傳Wrong Argument.
 */
