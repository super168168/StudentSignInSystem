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

# ����Ϊmatlab�汾
    # eng = matlab.engine.start_matlab()
    # # eng.recog(nargout=0)
    # recname=eng.recog()
    # print(recname)

# ����Ϊpython�汾
    recname = testgmm.gmmem()

    return recname

if __name__ == "__main__":
    # wavtra()
    wavrec()