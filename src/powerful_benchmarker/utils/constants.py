BAYESIAN_KEYWORDS = ("~BAYESIAN~", "~LOG_BAYESIAN~", "~INT_BAYESIAN~")
RESUME_FAILURE = "RESUME_FAILURE"
NON_META = "non_meta"
UNTRAINED_TRUNK = "untrained_trunk"
UNTRAINED_TRUNK_INT = -1
UNTRAINED_TRUNK_AND_EMBEDDER = "untrained_trunk_and_embedder"
UNTRAINED_TRUNK_AND_EMBEDDER_INT = 0
TRAINED = "trained"
TRAINED_STATUS_COL_NAME = "trained_status"
UNTRAINED_TRUNK_ALIASES = [str(UNTRAINED_TRUNK_INT), UNTRAINED_TRUNK_INT, UNTRAINED_TRUNK]
UNTRAINED_TRUNK_AND_EMBEDDER_ALIASES = [str(UNTRAINED_TRUNK_AND_EMBEDDER_INT), UNTRAINED_TRUNK_AND_EMBEDDER_INT, UNTRAINED_TRUNK_AND_EMBEDDER] 
TRAINED_ALIASES = ["best", TRAINED]
IGNORE_UNTRAINED_TRUNK = (UNTRAINED_TRUNK_INT,)
IGNORE_ALL_UNTRAINED = (UNTRAINED_TRUNK_INT, UNTRAINED_TRUNK_AND_EMBEDDER_INT)
CONFIG_DIFF_BASE_FOLDER_NAME = "resume_training_config_diffs_"