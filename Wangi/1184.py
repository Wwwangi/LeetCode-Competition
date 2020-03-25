class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total=sum(distance)
        minn=min(start,destination)
        maxx=max(start,destination)
        clock=sum(distance[minn:maxx])
        anticlock=total-clock
        return min(clock,anticlock)