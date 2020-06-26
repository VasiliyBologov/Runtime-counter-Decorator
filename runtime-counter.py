from datetime import datetime

def RunTimeCount(function_to_decorate):
    def the_wrapper_around_the_original_function():
        try:
            t_ = datetime.now()
            print("Start Def in: " + str(t_.strftime("%H:%M:%S")))
            function_to_decorate()
            t = datetime.now()
            print("End Def in: " + str(t.strftime("%H:%M:%S")))
            td = t - t_
            print('Runtime {} hour {} min  {} sec'.format(str(td.total_seconds() // 3600),
                                                              str(td.total_seconds() // 60), str(
                    td.total_seconds() - ((td.total_seconds() // 3600) * 3600) + ((td.total_seconds() // 60) * 60))))
            if td.total_seconds() < 60:
                print('Runtime  {} sec'.format(str(td.total_seconds())))
            elif td.total_seconds() > 60 and td.total_seconds() < 3600:
                print('Runtime  {} min'.format(str(td.total_seconds() // 60)))
            else:
                print('Runtime  {} h'.format(str(td.total_seconds() // 3600)))
        except:
            print("Somebody error ")
    return the_wrapper_around_the_original_function
