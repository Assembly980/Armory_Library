namespace Weapon_Armory.Data
{
    public class WeatherForecastService
    {
        public string Rarity { get; set; }
        public string PotionType { get; set; }
        public string Picture { get; set; }

        public WeatherForecastService()
        {
            Rarity = "WIP";
            PotionType = "WIP";
            Picture = "WIP";
        }

        public WeatherForecastService(string rarity, string potionType, string picture)
        {
            Rarity = rarity;
            PotionType = potionType;
            Picture = picture;
        }
    }
}