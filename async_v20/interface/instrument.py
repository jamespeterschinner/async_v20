from .decorators import endpoint
from ..definitions.primitives import InstrumentName
from ..definitions.types import CandlestickGranularity
from ..definitions.types import PriceComponent
from ..definitions.types import WeeklyAlignment
from ..endpoints.annotations import AlignmentTimezone
from ..endpoints.annotations import Count
from ..endpoints.annotations import DailyAlignment
from ..endpoints.annotations import FromTime
from ..endpoints.annotations import IncludeFirstQuery
from ..endpoints.annotations import Smooth
from ..endpoints.annotations import ToTime
from ..endpoints.instrument import *

__all__ = ['InstrumentInterface']


class InstrumentInterface(object):
    @endpoint(GETInstrumentsCandles)
    def get_candles(self,
                    instrument: InstrumentName,
                    price: PriceComponent = 'M',
                    granularity: CandlestickGranularity = 'S5',
                    count: Count = 500,
                    from_time: FromTime = ...,
                    to_time: ToTime = ...,
                    smooth: Smooth = False,
                    include_first_query: IncludeFirstQuery = True,
                    daily_alignment: DailyAlignment = 17,
                    alignment_timezone: AlignmentTimezone = 'America/New_York',
                    weekly_alignment: WeeklyAlignment = 'Friday',
                    ):
        """
        Fetch candlestick data for an instrument.

        Args:

            include_first_query: :class:`~async_v20.endpoints.annotations.IncludeFirstQuery`
            instrument: :class:`~async_v20.definitions.primitives.InstrumentName`
                Name of the Instrument
            price: :class:`~async_v20.endpoints.annotations.PriceComponent`
                The Price component(s) to get candlestick data for. Can contain
                any combination of the characters "M" (midpoint candles) "B"
                (bid candles) and "A" (ask candles).
            granularity: :class:`~async_v20.endpoints.annotations.CandlestickGranularity`
                The granularity of the candlesticks to fetch
            count: :class:`~async_v20.endpoints.annotations.Count`
                The number of candlesticks to return in the reponse. Count
                should not be specified if both the start and end parameters
                are provided, as the time range combined with the graularity
                will determine the number of candlesticks to return.
            from_time: :class:`~async_v20.endpoints.annotations.FromTime`
                The start of the time range to fetch candlesticks for.
            to_time: :class:`~async_v20.endpoints.annotations.ToTime`
                The end of the time range to fetch candlesticks for.
            smooth: :class:`~async_v20.endpoints.annotations.Smooth`
                A flag that controls whether the candlestick is "smoothed" or
                not.  A smoothed candlestick uses the previous candle's close
                price as its open price, while an unsmoothed candlestick uses
                the first price from its time range as its open price.
            daily_alignment: :class:`~async_v20.endpoints.annotations.DailyAlignment`
                The hour of the day (in the specified timezone) to use for
                granularities that have daily alignments.
            alignment_timezone: :class:`~async_v20.endpoints.annotations.AlignmentTimezone`
                The timezone to use for the dailyAlignment parameter.
                Candlesticks with daily alignment will be aligned to the
                dailyAlignment hour within the alignmentTimezone.
            weekly_alignment: :class:`~async_v20.definitions.primitives.WeeklyAlignment`
                The day of the week used for granularities that have weekly
                alignment.

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (instrument= :class:`~async_v20.definitions.primitives.InstrumentName`,
                granularity= :class:`~async_v20.definitions.primitives.CandlestickGranularity`,
                candles= :class:`~async_v20.definitions.types.ArrayCandlestick`)

        """
        pass
