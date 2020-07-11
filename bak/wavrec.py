import matlab
import matlab.engine

eng = matlab.engine.start_matlab()
eng.train(nargout=0)