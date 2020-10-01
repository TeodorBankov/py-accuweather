welcome_ascii = [""" ___            ___                                   _    _             
| . \ _ _  ___ | . | ___  ___  _ _  _ _ _  ___  ___ _| |_ | |_  ___  _ _ 
|  _/| | ||___||   |/ | '/ | '| | || | | |/ ._><_> | | |  | . |/ ._>| '_>
|_|  `_. |     |_|_|\_|_.\_|_.`___||__/_/ \___.<___| |_|  |_|_|\___.|_|  
     <___'                                                               
          By Teodor Bankov. Github: https://github.com/TeodorBankov
               Used Accuweather api from https://accuweather.com    """,
          """   ___               _                                     _   _               
  / _ \_   _        /_\   ___ ___ _   ___      _____  __ _| |_| |__   ___ _ __ 
 / /_)/  | | |_____ //_\\ / __/ __| | | \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__|
/ ___/| |_| |_____/  _  \ (_| (__| |_| |\ V  V /  __/ (_| | |_| | | |  __/ |   
\/     \__, |     \_/ \_/\___\___|\__,_| \_/\_/ \___|\__,_|\__|_| |_|\___|_|   
       |___/                                                                   
          By Teodor Bankov. Github: https://github.com/TeodorBankov
               Used Accuweather api from https://accuweather.com    """,
          """
.__         .__.                      , .        
[__)  . ___ [__] _. _.. ..    , _  _.-+-|_  _ ._.
|   \_|     |  |(_.(_.(_| \/\/ (/,(_] | [ )(/,[  
    ._|                                          
By Teodor Bankov. Github: https://github.com/TeodorBankov
    Used Accuweather api from https://accuweather.com    """]


# 0 - cloudy, Dreary (Overcast), Fog
# 1 - mostly cloudy
# 2 - partly sunny, Intermittent Clouds, Hazy Sunshine
# 3 - mostly sunny
# 4 - sunny
# 5 - showers (I have to enter that it could be mostly cloudy or mostly cloudy), rain
# 6 - t-storm (Also could be mostly or partly cloudy)
# 7 - flurries (mostly cloudy/ partly cloudy also included here), snow, mostly cloudy with snow, 
# 8 - freezing rain, sleet, ice, ice with snow
# 9 - cold thermometer
# 10 - hot thermometer
# 11 - windy
# For the moon the same weather ascii art could be used as the sun
forecast_ascii = ["""
          .-~~~-.
  .- ~ ~-(       )_ _
 /                    ~ -.
|                          ',
 \                         .'
   ~- ._ ,. ,.,.,., ,.. -~  """,
   """
                   _                                  
              (`  ).                   _           
             (     ).              .:(`  )`.       
)           _(       '`.          :(   .    )      
        .=(`(      .   )     .--  `.  (    ) )      
       ((    (..__.:'-'   .+(   )   ` _`  ) )                 
`.     `(       ) )       (   .  )     (   )  ._   
  )      ` __.:'   )     (   (   ))     `-'.-(`  ) 
)  )  ( )       --'       `- __.'         :(      )) 
.-'  (_.'          .')                    `(    )  ))
                  (_  )                     ` __.:'          
                                        
--..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--. """,
"""
              .
               					
              |					
     .               /				
      \       I     				
                  /
        \  ,g88R_
          d888(`  ).                   _
 -  --==  888(     ).=--           .+(`  )`.
)         Y8P(       '`.          :(   .    )
        .+(`(      .   )     .--  `.  (    ) )
       ((    (..__.:'-'   .=(   )   ` _`  ) )
`.     `(       ) )       (   .  )     (   )  ._
  )      ` __.:'   )     (   (   ))     `-'.:(`  )
)  )  ( )       --'       `- __.'         :(      ))
.-'  (_.'          .')                    `(    )  ))
                  (_  )                     ` __.:'
                                        	
--..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--. """,
"""
           |
     \     |     /
       \       /
         ,d8b,           .,
 (')-")_ 88888 ---   ;';'  ';'.
('-  (. ')98P'      ';.,;    ,;
 '-.(PjP)'     \       '.';.'
           |     \
           | """,
"""
      ;   :   ;
   .   \_,!,_/   ,
    `.,'     `.,'
     /         \
~ -- :         : -- ~
     \         /
    ,'`._   _.'`.
   '   / `!` \   `
      ;   :   ;   """,
"""
                             000      00
                           0000000   0000
              0      00  00000000000000000
            0000 0  000000000000000000000000       0
         000000000000000000000000000000000000000 000
        0000000000000000000000000000000000000000000000
    000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000
              / / / / / / / / / / / / / / / /
            / / / / / / / / / / / / / / /
            / / / / / / / / / / / / / / /
          / / / / / / / / / / / / / /
          / / / / / / / / / / / / /
        / / / / / / / / / / / /
        / / / / / / / / / /

         ...........    """,
"""
    ___(                        )
   (                          _)
  (_                       __))
    ((                _____)
      (_________)----'
         _/  /
        /  _/
      _/  /
     / __/
   _/ /
  /__/
 //
/  """,
"""
                     *  .  *
                   . _\/ \/_ .
                    \  \ /  /             .      .
      ..    ..    -==>: X :<==-           _\/  \/_
      '\    /'      / _/ \_ \              _\/\/_
        \\//       '  /\ /\  '         _\_\_\/\/_/_/_
   _.__\\\///__._    *  '  *            / /_/\/\_\ \
    '  ///\\\  '                           _/\/\_
        //\\                               /\  /\
      ./    \.             ._    _.       '      '
      ''    ''             (_)  (_)                  <> \  / <>
                            .\::/.                   \_\/  \/_/
           .:.          _.=._\\//_.=._                  \\//
      ..   \o/   ..      '=' //\\ '='             _<>_\_\<>/_/_<>_
      :o|   |   |o:         '/::\'                 <> / /<>\ \ <>
       ~ '. ' .' ~         (_)  (_)      _    _       _ //\\ _
           >O<             '      '     /_/  \_\     / /\  /\ \
       _ .' . '. _                        \\//       <> /  \ <>
      :o|   |   |o:                   /\_\\><\\ \/
           ':'        . ~~\  /~~ .       _//\\_
jgs                   _\_._\/_._/_      \_\  /_/
                       / ' /\ ' \                   \o/
       o              ' __/  \__ '              _o/.:|:.\o_
  o    :    o         ' .'|  |'.                  .\:|:/.
    '.\'/.'                 .                 -=>>::>o<::<<=-
    :->@<-:                 :                   _ '/:|:\' _
    .'/.\'.           '.___/*\___.'              o\':|:'/o
  o    :    o           \* \ / */                   /o\
       o                 >--X--<
                        /*_/ \_*\
                      .'   \*/   '.
                            :
                            ' """,
"""
                ()
                /\
               //\\
              <<  >>
          ()   \\//   ()
()._____   /\   \\   /\   _____.()
   \.--.\ //\\ //\\ //\\ /.--./
    \\__\\/__\//__\//__\\/__//
     '--/\\--//\--//\--/\\--'
        \\\\///\\//\\\////
    ()-= >>\\< <\\> >\\<< =-()
        ////\\\//\\///\\\\
     .--\\/--\//--\//--\//--.
    //""/\\""//\""//\""//\""\\
   /'--'/ \\// \\// \\// \'--'\
 ()`" "`   \/   //   \/   `" "`()
          ()   //\\   ()
              <<  >>
               \\//
                \/
                ()""",
"""
                            ______________________
                            |   ^F     _    ^C   |
                            |  100  - | | -  40  |
                            |   90  - | | -  30  |
                            |   80  - | | -  25  |
                            |   70  - | | -  20  |
                            |   60  - | | -  15  |
                            |   50  - | | -  10  |
                            |   40  - | | -   5  |
                            |   30  - | | -   0  |
                            |   20  - | | -  -5  |
                            |   10  - | | - -10  |
                            |    0  - | | - -20  |
                            |  -10  - | | - -25  |
                            |  -20  - |*| - -30  |
                            |  -30  - |*| - -35  |
                            |        '***`       |
                            |       (*****)      |
                            |        `---'       |
                            |____________________| """,
"""
                            ______________________
                            |   ^F     _    ^C   |
                            |  100  - | | -  40  |
                            |   90  - | | -  30  |
                            |   80  - |*| -  25  |
                            |   70  - |*| -  20  |
                            |   60  - |*| -  15  |
                            |   50  - |*| -  10  |
                            |   40  - |*| -   5  |
                            |   30  - |*| -   0  |
                            |   20  - |*| -  -5  |
                            |   10  - |*| - -10  |
                            |    0  - |*| - -20  |
                            |  -10  - |*| - -25  |
                            |  -20  - |*| - -30  |
                            |  -30  - |*| - -35  |
                            |        '***`       |
                            |       (*****)      |
                            |        `---'       |
                            |____________________| """,
"""
   ((  "####@@!!$$    ))
       `#####@@!$$`  ))
    ((  '####@!!$:
   ((  ,####@!!$:   ))
       .###@!!$:
       `##@@!$:
        `#@!!$
  !@#    `#@!$:       @#$
   #$     `#@!$:       !@!
            '@!$:
        '`\   "!$: /`'
           '\  '!: /'
             "\ : /"
  -."-/\\\-."//.-"/:`\."-.JrS"."-=_\\
" -."-.\\"-."//.-".`-."_\\-.".-\".-//  """]

#print(welcome_ascii[1])