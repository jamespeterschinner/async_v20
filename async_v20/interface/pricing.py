from .decorators import endpoint
from ..definitions.primitives import DateTime
from ..endpoints.annotations import *
from ..endpoints.pricing import *

__all__ = ['PricingInterface']


class PricingInterface(object):
    @endpoint(GETPricing)
    def get_pricing(self,
                    instruments: Instruments = ...,
                    since: DateTime = ...):
        """
        Get pricing information for a specified list of Instruments within an
        Account.

        Args:

            instruments: :class:`~async_v20.endpoints.annotations.Instruments`
            list of Instruments to get pricing for.
            since: :class:`~async_v20.definitions.primitives.DateTime`
                Date/Time filter to apply to the returned prices. Only prices
                with a time later than this filter will be provided.

        Returns:

            **status [200]**
            :class:`~async_v20.interface.response.Response`
            (prices= :class:`~async_v20.definitions.types.ArrayPrice`,
            time= :class:`~async_v20.definitions.primitives.DateTime`)

        """
        pass

    @endpoint(GETPricingStream)
    def stream_pricing(self,
                       instruments: Instruments = ...,
                       snapshot: Snapshot = ...):
        """
        Get a stream of Account Prices starting from when the request is made.
        This pricing stream does not include every single price created for the
        Account, but instead will provide at most 4 prices per second (every
        250 milliseconds) for each instrument being requested. If more than one
        price is created for an instrument during the 250 millisecond window,
        only the price in effect at the end of the window is sent. This means
        that during periods of rapid price movement, subscribers to this stream
        will not be sent every price. Pricing windows for different connections
        to the price stream are not all aligned in the same way (i.e. they are
        not all aligned to the top of the second). This means that during
        periods of rapid price movement, different subscribers may observe
        different prices depending on their alignment.

        Args:

            instruments: :class:`~async_v20.endpoints.annotations.Instruments`
            list of Instruments to stream Prices for.
            snapshot: :class:`~async_v20.endpoints.annotations.Snapshot`
                Flag that enables/disables the sending of a pricing snapshot
                when initially connecting to the stream.

        Returns:

            **status [200]**
            :class:`~async_v20.interface.response.Response`
            (PRICE= :class:`~async_v20.definitions.types.Price`)

                **OR**

            :class:`~async_v20.interface.response.Response`
            (HEARTBEAT= :class:`~async_v20.definitions.types.PricingHeartbeat`)


        """
        pass
