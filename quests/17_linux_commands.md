PS C:\Users\PC> cd C:\Commands
PS C:\Commands> pwd

Path
----
C:\Commands


PS C:\Commands> mkdir Test


    디렉터리: C:\Commands


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----      2025-11-06   오후 5:47                Test


PS C:\Commands> ls


    디렉터리: C:\Commands


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----      2025-11-06   오후 5:47                Test


PS C:\Commands> mkdir Notes


    디렉터리: C:\Commands


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----      2025-11-06   오후 5:48                Notes


PS C:\Commands> cd Notes
PS C:\Commands\Notes> pwd

Path
----
C:\Commands\Notes


PS C:\Commands\Notes> cd ..
PS C:\Commands> mkdir Images, Videos, Docs


    디렉터리: C:\Commands


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----      2025-11-06   오후 5:49                Images
d-----      2025-11-06   오후 5:49                Videos
d-----      2025-11-06   오후 5:49                Docs


PS C:\Commands> ls


    디렉터리: C:\Commands


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----      2025-11-06   오후 5:49                Docs
d-----      2025-11-06   오후 5:49                Images
d-----      2025-11-06   오후 5:48                Notes
d-----      2025-11-06   오후 5:47                Test
d-----      2025-11-06   오후 5:49                Videos


PS C:\Commands> cd Docs
PS C:\Commands\Docs> ..
.. : '..' 용어가 cmdlet, 함수, 스크립트 파일 또는 실행할 수 있는 프로그램 이름으로 인식되지 않습니다. 이름이 정확한지 확인하고 경로가
 포함된 경우 경로가 올바른지 검증한 다음 다시 시도하십시오.
위치 줄:1 문자:1
+ ..
+ ~~
    + CategoryInfo          : ObjectNotFound: (..:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Commands\Docs> cd ..
PS C:\Commands> ls


    디렉터리: C:\Commands


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----      2025-11-06   오후 5:49                Docs
d-----      2025-11-06   오후 5:49                Images
d-----      2025-11-06   오후 5:48                Notes
d-----      2025-11-06   오후 5:47                Test
d-----      2025-11-06   오후 5:49                Videos


PS C:\Commands>
