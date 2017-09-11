from .decorators import endpoint
from ..endpoints.instrument import *

class InstrumentInterface(object):

    @endpoint(GETInstrumentsCandles)
    def get_candles(self,
                instrument: Instrument,
                price: Price,
                granularity: CandlestickGranularity,
                count: Count,
                from_: FromDateTime,
                to: ToDateTime,
                smooth: Smooth,
                includeFirst: Incluclassirst,
                dailyAlignment: DailyAlignment,
                alignmentTimezone: AlignmentTimezone,
                weeklyAlignment: WeeklyAlignment,
    ):
        """
        Fetch candlestick data for an instrument.

        Args:
            instrument:
                Name of the Instrument
            price:
                The Price component(s) to get candlestick data for. Can contain
                any combination of the characters "M" (midpoint candles) "B"
                (bid candles) and "A" (ask candles).
            granularity:
                The granularity of the candlesticks to fetch
            count:
                The number of candlesticks to return in the reponse. Count
                should not be specified if both the start and end parameters
                are provided, as the time range combined with the graularity
                will determine the number of candlesticks to return.
            fromTime:
                The start of the time range to fetch candlesticks for.
            toTime:
                The end of the time range to fetch candlesticks for.
            smooth:
                A flag that controls whether the candlestick is "smoothed" or
                not.  A smoothed candlestick uses the previous candle's close
                price as its open price, while an unsmoothed candlestick uses
                the first price from its time range as its open price.
            includeFirst:
                A flag that controls whether the candlestick that is covered by
                the from time should be included in the results. This flag
                enables clients to use the timestamp of the last completed
                candlestick received to poll for future candlesticks but avoid
                receiving the previous candlestick repeatedly.
            dailyAlignment:
                The hour of the day (in the specified timezone) to use for
                granularities that have daily alignments.
            alignmentTimezone:
                The timezone to use for the dailyAlignment parameter.
                Candlesticks with daily alignment will be aligned to the
                dailyAlignment hour within the alignmentTimezone.
            weeklyAlignment:
                The day of the week used for granularities that have weekly
                alignment.

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """
        pass