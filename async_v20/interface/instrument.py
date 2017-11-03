from .decorators import endpoint
from ..definitions.primitives import InstrumentName
from ..definitions.types import CandlestickGranularity
from ..definitions.types import PriceComponent
from ..definitions.types import WeeklyAlignment
from ..endpoints.annotations import AlignmentTimezone
from ..endpoints.annotations import Count
from ..endpoints.annotations import DailyAlignment
from ..endpoints.annotations import FromTime
from ..endpoints.annotations import Smooth
from ..endpoints.annotations import ToTime
from ..endpoints.annotations import IncludeFirstQuery
from ..endpoints.instrument import *

__all__ = ['InstrumentInterface']


class InstrumentInterface(object):
    @endpoint(GETInstrumentsCandles)
    def get_candles(self,
                    instrument: InstrumentName,
                    price: PriceComponent = 'M',
                    granularity: CandlestickGranularity = 'S5',
                    count: Count = 500,
                    from_time: FromTime = None,
                    to_time: ToTime = None,
                    smooth: Smooth = False,
                    include_first_query: IncludeFirstQuery = True,
                    daily_alignment: DailyAlignment = 17,
                    alignment_timezone: AlignmentTimezone = 'America/New_York',
                    weekly_alignment: WeeklyAlignment = 'Friday',
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
            from_time:
                The start of the time range to fetch candlesticks for.
            to_time:
                The end of the time range to fetch candlesticks for.
            smooth:
                A flag that controls whether the candlestick is "smoothed" or
                not.  A smoothed candlestick uses the previous candle's close
                price as its open price, while an unsmoothed candlestick uses
                the first price from its time range as its open price.
            include_first:
                A flag that controls whether the candlestick that is covered by
                the from time should be included in the results. This flag
                enables clients to use the timestamp of the last completed
                candlestick received to poll for future candlesticks but avoid
                receiving the previous candlestick repeatedly.
            daily_alignment:
                The hour of the day (in the specified timezone) to use for
                granularities that have daily alignments.
            alignment_timezone:
                The timezone to use for the dailyAlignment parameter.
                Candlesticks with daily alignment will be aligned to the
                dailyAlignment hour within the alignmentTimezone.
            weekly_alignment:
                The day of the week used for granularities that have weekly
                alignment.

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass
