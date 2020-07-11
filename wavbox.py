# import matlab
# import matlab.engine
import luyin
import traluyin
import testgmm
# def wavtra():
    # eng = matlab.engine.start_matlab()
    # eng.train(nargout=0)

def wavrec():
    luyin.my_record()

# 以下为matlab版本
    # eng = matlab.engine.start_matlab()
    # # eng.recog(nargout=0)
    # recname=eng.recog()
    # print(recname)

# 以下为python版本
    recname = testgmm.gmmem()

    return recname

if __name__ == "__main__":
    # wavtra()
    wavrec()