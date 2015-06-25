from toontown.toonbase import ToontownGlobals, TTLocalizer
import calendar, datetime

TRICK_OR_TREAT = 0
WINTER_CAROLING = 1
CAROLING_REWARD = 100
SCAVENGER_HUNT_LOCATIONS = 6

Holidays = {
    ToontownGlobals.LAUGHING_MAN: {
        'startMonth': 6,
        'startDay': 22,
        'endMonth': 6,
        'endDay': 22,
        'startMessage': TTLocalizer.LaughingManHolidayStart,
        'ongoingMessage': TTLocalizer.LaughingManHolidayOngoing,
        'endMessage': TTLocalizer.LaughingManHolidayEnd
    },
    ToontownGlobals.GRAND_PRIX: {
        'weekDay': 0,
        'startMessage': TTLocalizer.CircuitRaceStart,
        'ongoingMessage': TTLocalizer.CircuitRaceOngoing,
        'endMessage': TTLocalizer.CircuitRaceEnd
    },
    ToontownGlobals.FISH_BINGO: {
        'weekDay': 2,
        'startMessage': TTLocalizer.FishBingoStart,
        'ongoingMessage': TTLocalizer.FishBingoOngoing,
        'endMessage': TTLocalizer.FishBingoEnd
    },
    ToontownGlobals.SILLY_SATURDAY: {
        'weekDay': 5,
        'startMessage': TTLocalizer.SillySaturdayStart,
        'ongoingMessage': TTLocalizer.SillySaturdayOngoing,
        'endMessage': TTLocalizer.SillySaturdayEnd
    },
    ToontownGlobals.BLACK_CAT_DAY: {
        'startDay': 13,
        'endDay': 13,
        'startMessage': TTLocalizer.BlackCatHolidayStart,
        'ongoingMessage': TTLocalizer.BlackCatHolidayStart,
        'endMessage': TTLocalizer.BlackCatHolidayEnd
    },
    ToontownGlobals.APRIL_TOONS_WEEK: {
        'startMonth': 4,
        'startDay': 1,
        'endMonth': 4,
        'endDay': 7,
        'startMessage': TTLocalizer.AprilToonsWeekStart,
        'ongoingMessage': TTLocalizer.AprilToonsWeekStart,
        'endMessage': TTLocalizer.AprilToonsWeekEnd
    },
    ToontownGlobals.IDES_OF_MARCH: {
        'startMonth': 3,
        'startDay': 14,
        'endMonth': 3,
        'endDay': 20,
        'startMessage': TTLocalizer.IdesOfMarchStart,
        'ongoingMessage': TTLocalizer.IdesOfMarchStart,
        'endMessage': TTLocalizer.IdesOfMarchEnd,
        'speedchatIndexes': [30450], # It's easy to be green!
        'effectMessage': TTLocalizer.GreenToonEffectMsg,
        'effectDelay': 10
    },
    ToontownGlobals.CHRISTMAS: {
        """'startMonth': 12,
        'startDay': 14,
        'endMonth': 1,
        'endDay': 4,"""
        'startMessage': TTLocalizer.WinterCarolingStart,
        'ongoingMessage': TTLocalizer.WinterCarolingStart,
        'endMessage': TTLocalizer.WinterCarolingEnd,
        'speedchatIndexes': range(30200, 30206),
        'effectDelay': 15,
        'scavengerHunt': WINTER_CAROLING
    },
    ToontownGlobals.HALLOWEEN: {
        'startMonth': 10,
        'startDay': 13,
        'endMonth': 10,
        'endDay': 31,
        'startMessage': TTLocalizer.TrickOrTreatStart,
        'ongoingMessage': TTLocalizer.TrickOrTreatStart,
        'endMessage': TTLocalizer.TrickOrTreatEnd,
        'speedchatIndexes': [10003],
        'effectDelay': 15,
        'scavengerHunt': TRICK_OR_TREAT
    }
}

def getHoliday(id):
    return Holidays.get(id, {})

def getServerTime(date):
    epoch = datetime.datetime.fromtimestamp(0, base.cr.toontownTimeManager.serverTimeZone)
    delta = date - epoch

    return delta.total_seconds()

def getStartDate(holiday, year=None):
    if 'startDate' in holiday:
        return holiday['startDate']

    rightNow = datetime.datetime.now()
    startMonth = holiday['startMonth'] if 'startMonth' in holiday else (rightNow.month if 'weekDay' in holiday else 1)
    startDay = holiday['startDay'] if 'startDay' in holiday else (rightNow.day if 'weekDay' in holiday else calendar.monthrange(rightNow.year, startMonth)[0])
    startDate = datetime.datetime(year if year else rightNow.year, startMonth, startDay, tzinfo=base.cr.toontownTimeManager.serverTimeZone)
    holiday['startDate'] = startDate
    
    return startDate

def getEndDate(holiday, year=None):
    if 'endDate' in holiday:
        return holiday['endDate']

    rightNow = datetime.datetime.now()
    endMonth = holiday['endMonth'] if 'endMonth' in holiday else (rightNow.month if 'weekDay' in holiday else 12)
    endDay = holiday['endDay'] if 'endDay' in holiday else (rightNow.day if 'weekDay' in holiday else calendar.monthrange(rightNow.year, endMonth)[1])
    endYear = year if year else rightNow.year

    if 'startMonth' in holiday and holiday['startMonth'] > endMonth:
        endYear += 1

    endDate = datetime.datetime(endYear, endMonth, endDay, tzinfo=base.cr.toontownTimeManager.serverTimeZone)
    holiday['endDate'] = endDate

    return endDate