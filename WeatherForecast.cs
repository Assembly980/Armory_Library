namespace Weapon_Armory.Data
{
    public class WeatherForecast
    {
        public string WeaponRarity { get; set; }

        public string WeaponName { get; set; }
        public string? Description { get; set; }
        public string Picture { get; set; }

        public WeatherForecast()
        {
            WeaponRarity = "WIP";
            WeaponName = "WIP";
            Description = "WIP";
            Picture = "WIP";
        }

        public WeatherForecast(string rarity, string weaponName, string? description, string picture)
        {
            WeaponRarity = rarity;
            WeaponName = weaponName;
            Description = description;
            Picture = picture;
        }
    }
}