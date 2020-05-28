import readHTML

errors = []
redlist = ['http://www.satstar.net/maps/images/horizons2_seasia_world.gif', 'http://www.satstar.net/maps/images/skyterra1_lem6_world.gif', 'http://www.satstar.net/maps/images/skyterra1_ltp1.gif', 'http://www.satstar.net/maps/images/echo16_sp13_2.gif']
if __name__=="__main__":
    #readHTML.getHTML(r"http://www.satstar.net/satellites/intel33e.html")
    readHTML.downPic(redlist)
    print(errors)
