import numpy as np

vectorGroundTruth = np.load("./documentation/CI_CD_results/signals_GroundTruth/FID_signal.npz")
vectorLastPush = np.load("./documentation/CI_CD_results/signals_CICD_last_run/FID_signal.npz")

vectorGroundTruth = vectorGroundTruth['signal'].astype(np.complex64)
vectorLastPush = vectorLastPush['signal'].astype(np.complex64)

class TestPythonScript:

    def test_compare_PlaygroundMR0_results(self):
        assert np.array_equal(vectorGroundTruth, vectorLastPush)

