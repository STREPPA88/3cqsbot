import argparse
import configparser
import os
import subprocess

port = os.getenv('PORT', default=5000)
print(port)

parser = argparse.ArgumentParser(
    description="3CQSBot bringing 3CQS signals to 3Commas."
)
parser.add_argument("--host", default="0.0.0.0", type=str)
parser.add_argument("--port", default=port, type=int)
parser.add_argument(
    "-l",
    "--loglevel",
    metavar="loglevel",
    type=str,
    nargs="?",
    default="info",
    help="loglevel during runtime - use info, debug, warning, ...",
)

args = parser.parse_args()

config = configparser.ConfigParser()

config.add_section('general')
config.add_section('telegram')
config.add_section('commas')
config.add_section('dcabot')
config.add_section('trading')
config.add_section('filter')

config['general']['debug'] =  str(os.getenv("GE_DEBUG"))
config['general']['log_to_file'] =  str(os.getenv("GE_LOGFILE"))
config['general']['log_file_path'] =  str(os.getenv("GE_LOGFILEPATH"))
config['general']['log_file_size'] =  str(os.getenv("GE_LOGFILESIZE"))
config['general']['log_file_count'] =  str(os.getenv("GE_LOGFILECOUNT"))

config['telegram']['api_id'] =  str(os.getenv("TG_ID"))
config['telegram']['api_hash'] =  str(os.getenv("TG_HASH"))
config['telegram']['sessionfile'] =  str(os.getenv("TG_SESSIONFILE"))
config['telegram']['chatroom'] =  str(os.getenv("TG_CHATROOM"))

config['commas']['key'] =  str(os.getenv("API_KEY"))
config['commas']['secret'] =  str(os.getenv("API_SECRET"))
config['commas']['timeout'] =  str(os.getenv("API_TIMEOUT"))
config['commas']['retries'] =  str(os.getenv("API_RETRIES"))
config['commas']['delay_between_retries'] =  str(os.getenv("API_RETRY_DELAY"))
config['commas']['system_bot_value'] =  str(os.getenv("API_SYS_BOT_VALUE"))

config['dcabot']['prefix'] =  str(os.getenv("DCABOT_PREFIX"))
config['dcabot']['subprefix'] =  str(os.getenv("DCABOT_SUBPREFIX"))
config['dcabot']['suffix'] =  str(os.getenv("DCABOT_SUFFIX"))
config['dcabot']['tp'] =  str(os.getenv("DCABOT_TP"))
config['dcabot']['bo'] =  str(os.getenv("DCABOT_BO"))
config['dcabot']['so'] =  str(os.getenv("DCABOT_SO"))
config['dcabot']['os'] =  str(os.getenv("DCABOT_OS"))
config['dcabot']['ss'] =  str(os.getenv("DCABOT_SS"))
config['dcabot']['sos'] =  str(os.getenv("DCABOT_SOS"))
config['dcabot']['mad'] =  str(os.getenv("DCABOT_MAD"))
config['dcabot']['max'] =  str(os.getenv("DCABOT_MAX"))
config['dcabot']['mstc'] =  str(os.getenv("DCABOT_MSTC"))
config['dcabot']['sdsp'] =  str(os.getenv("DCABOT_SDSP"))
config['dcabot']['single'] =  str(os.getenv("DCABOT_SINGLE"))
config['dcabot']['single_count'] =  str(os.getenv("DCABOT_SINGLE_COUNT"))
config['dcabot']['btc_min_vol'] =  str(os.getenv("DCABOT_BTC_MIN_VOL"))
config['dcabot']['cooldown'] =  str(os.getenv("DCABOT_COOLDOWN"))
config['dcabot']['deals_count'] =  str(os.getenv("DCABOT_DEALS_COUNT"))

config['trading']['market'] =  str(os.getenv("TD_MARKET"))
config['trading']['trade_mode'] =  str(os.getenv("TD_TRADE_MODE"))
config['trading']['account_name'] =  str(os.getenv("TD_ACCOUNT"))
config['trading']['delete_single_bots'] =  str(os.getenv("TD_DELETE_SINGLE"))
config['trading']['singlebot_update'] =  str(os.getenv("TD_UPDATE_SINGLE"))
config['trading']['trailing'] =  str(os.getenv("TD_TRAILING"))
config['trading']['trailing_deviation'] =  str(os.getenv("TD_TRAILING_DEVIATION"))
config['trading']['trade_future'] =  str(os.getenv("TD_TRADE_FUTURE"))
config['trading']['leverage_type'] =  str(os.getenv("TD_LEVERAGE_TYPE"))
config['trading']['leverage_value'] =  str(os.getenv("TD_LEVERAGE_VALUE"))
config['trading']['stop_loss_percent'] =  str(os.getenv("TD_STOP_LOSS_PERCENT"))
config['trading']['stop_loss_type'] =  str(os.getenv("TD_STOP_LOSS_TYPE"))
config['trading']['stop_loss_timeout_enabled'] =  str(os.getenv("TD_STOP_LOSS_TIMEOUT_ENABLED"))
config['trading']['stop_loss_timeout_seconds'] =  str(os.getenv("TD_STOP_LOSS_TIMEOUT_SECONDS"))

config['filter']['symrank_signal'] =  str(os.getenv("FI_SYMRANK_SIGNAL"))
config['filter']['symrank_limit_min'] =  str(os.getenv("FI_SYMRANK_LIMIT_MIN"))
config['filter']['symrank_limit_max'] =  str(os.getenv("FI_SYMRANK_LIMIT_MAX"))
config['filter']['volatility_limit_min'] =  str(os.getenv("FI_VOLATILITY_LIMIT_MIN"))
config['filter']['volatility_limit_max'] =  str(os.getenv("FI_VOLATILITY_LIMIT_MAX"))
config['filter']['price_action_limit_min'] =  str(os.getenv("FI_PRICE_ACTION_LIMIT_MIN"))
config['filter']['price_action_limit_max'] =  str(os.getenv("FI_PRICE_ACTION_LIMIT_MAX"))
config['filter']['topcoin_filter'] =  str(os.getenv("FI_TOPCOIN_FILTER"))
config['filter']['topcoin_volume'] =  str(os.getenv("FI_TOPCOIN_LIMIT"))
config['filter']['topcoin_limit'] =  str(os.getenv("FI_TOPCOIN_VOLUME"))
config['filter']['topcoin_exchange'] =  str(os.getenv("FI_TOPCOIN_EXCHANGE"))
config['filter']['limit_initial_pairs'] =  str(os.getenv("FI_LIMIT_INIT_PAIRS"))
config['filter']['random_pair'] =  str(os.getenv("FI_RANDOM_PAIR"))
config['filter']['deal_mode'] =  str(os.getenv("FI_DEAL_MODE"))
config['filter']['btc_pulse'] =  str(os.getenv("FI_BTC_PULSE"))
config['filter']['ext_botswitch'] =  str(os.getenv("FI_EXT_BOTSWITCH"))
config['filter']['token_denylist'] =  str(os.getenv("FI_DENYLIST"))

with open('config.cfg', 'w') as configfile:
    config.write(configfile)

subprocess.run("./3cqsbot.py", shell=True)