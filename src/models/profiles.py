

class Profile:

    def __init__(self, name: str, proxy: str, homepage: str):
        self.name = name
        self.proxy = proxy
        self.homepage = homepage
    
    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.name == other.name and
                    self.proxy == other.proxy and
                    self.homepage == other.homepage)
        return NotImplemented
    
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "proxy": self.proxy,
            "homepage": self.homepage
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Profile":
        return cls(name= data["name"],
                   proxy= data.get("proxy"),
                   homepage= data.get("homepage")
        )
    


