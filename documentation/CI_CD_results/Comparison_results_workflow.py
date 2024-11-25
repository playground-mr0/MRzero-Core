import numpy as np
import os

#1. we go through each npz file in ./documentation/CI_CD_results/signals_GroundTruth
#2. we search for a file with identical name in folder ./documentation/CI_CD_results/signals_CICD_last_run
#3. we load the numpy arrays from these 2 files
#4. Compute difference and save logical value = difference
#5. For each diff we echo a message saying for which signal and if it passed or not
#6. The test final value will be the && operation between all the difs

folder_Ground_Truth = "./documentation/CI_CD_results/signals_GroundTruth"
folder_Last_Push = "./documentation/CI_CD_results/signals_CICD_last_run"

diff_total = True

for filename in os.listdir(folder_Ground_Truth):
    if filename.endswith('.npz'):
        file_path = os.path.join(folder_Ground_Truth, filename)
        print(f'Processing file: {file_path}')

        file_path_last_run = os.path.join(folder_Last_Push, filename)

        vectorGroundTruth = np.load(file_path)
        vectorLastPush = np.load(file_path_last_run)   

        vectorGroundTruth = vectorGroundTruth['signal'].astype(np.complex64)
        vectorLastPush = vectorLastPush['signal'].astype(np.complex64)

        diff_i = np.array_equal(vectorGroundTruth, vectorLastPush)

        print("For signal " + filename + " = ", diff_i)

        diff_total = diff_total & diff_i

class TestPythonScript:

    def test_compare_PlaygroundMR0_results(self):
        assert diff_total        

'''
vectorGroundTruth = np.load("./documentation/CI_CD_results/signals_GroundTruth/FID_signal.npz")
vectorLastPush = np.load("./documentation/CI_CD_results/signals_CICD_last_run/FID_signal.npz")

vectorGroundTruth = vectorGroundTruth['signal'].astype(np.complex64)
vectorLastPush = vectorLastPush['signal'].astype(np.complex64)

class TestPythonScript:

    def test_compare_PlaygroundMR0_results(self):
        assert np.array_equal(vectorGroundTruth, vectorLastPush)
'''
