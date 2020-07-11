import matlab
import matlab.engine

eng = matlab.engine.start_matlab()
# eng.recog(nargout=0)
recname=eng.recog()
print(recname)