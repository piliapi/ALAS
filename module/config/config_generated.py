import datetime

# This file was automatically generated by module/config/db.py.
# Don't modify it manually.


class GeneratedConfig:
    """
    Auto generated configuration
    """

    # Func `Alas`
    Scheduler_Enable = False
    Scheduler_NextRun = datetime.datetime(2020, 1, 1, 0, 0)
    Scheduler_Command = 'Alas'
    Scheduler_SuccessInterval = 0
    Scheduler_FailureInterval = 120
    Scheduler_ServerUpdate = '00:00'
    Emulator_Serial = '127.0.0.1:5555'
    Emulator_PackageName = 'com.bilibili.azurlane'
    Emulator_ScreenshotMethod = 'ADB'
    Emulator_ControlMethod = 'minitouch'
    Error_HandleError = True
    Error_SaveError = True
    Error_ScreenshotLength = 1
    DropRecord_SaveFolder = './screenshots'
    DropRecord_AzurStatsID = None
    DropRecord_SaveResearch = False
    DropRecord_UploadResearch = False
    DropRecord_SaveCommission = False
    DropRecord_UploadCommission = False
    DropRecord_SaveCombat = False

    # Func `Main`

    # Func `Commission`
    Commission_DoMajorCommission = False
    Commission_CommissionFilter = 'DailyEvent\n> Gem-8 > Gem-4 > Gem-2\n> Box-6 > Box-3 > Box-1\n> DailyCube-0:30 > UrgentCube-1:30 > DailyCube-1:30 > UrgentCube-1:40 > UrgentCube-2:15\n> UrgentCube-3 > DailyCube-3 > UrgentCube-4 > UrgentCube-6\n> Major\n> DailyRescource > DailyChip\n> UrgentBook-2:30 > UrgentBook-2 > UrgentBook-1:20 > UrgentBook-1:40\n> Daily-0:20 > Daily-0:30 > Daily-1:00 > Daily-1:30 > Daily-2:00\n> NightOil > NightCube\n> shortest'

    # Func `Tactical`
    Tactical_TacticalFilter = 'SameT3 > SameT2 > SameT1\n> BlueT2 > YellowT2 > RedT2\n> BlueT3 > YellowT3 > RedT3\n> BlueT1 > YellowT1 > RedT1\n> first'

    # Func `Research`
    Research_UseCube = False
    Research_UseCoin = True
    Research_UsePart = True
    Research_PresetFilter = 'series_4'
    Research_CustomFilter = '0.5 > reset > shortest'
