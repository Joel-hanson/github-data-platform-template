# GitHub Data Platform Template

Transform any data source into a free, automated API using GitHub Actions and GitHub Pages.

## Quick Start

1. **Fork this repository**
2. **Customize `src/scraper.py`** with your data source
3. **Update `.github/workflows/data-collection.yml`** with your schedule
4. **Enable GitHub Pages** in repository settings
5. **Your API is live!**

## Project Structure

```
├── .github/workflows/
│   └── data-collection.yml    # Automated data collection
├── src/
│   └── scraper.py            # Your data scraper
├── api/
│   ├── latest.json           # Latest data endpoint
│   └── latest.jsonp          # JSONP endpoint
├── data/
│   └── historical.json       # Historical data storage
├── docs/
│   └── index.html           # Dashboard/documentation
└── README.md
```

## Configuration

### 1. Update Your Data Source

Edit `src/scraper.py` to fetch data from your source:

```python
def scrape_data():
    """Replace this with your data source"""
    # Your scraping logic here
    url = "https://your-data-source.com/api"
    response = requests.get(url)
    return process_data(response.json())
```

### 2. Set Update Schedule

Modify `.github/workflows/data-collection.yml`:

```yaml
on:
  schedule:
    - cron: "0 6 * * *" # Daily at 6 AM UTC
    # Change to your preferred schedule
```

### 3. Customize API Output

The template generates these endpoints automatically:

- `https://raw.githubusercontent.com/username/repo/main/api/latest.json`
- `https://raw.githubusercontent.com/username/repo/main/api/latest.jsonp`

## Dashboard

Enable GitHub Pages to host your dashboard at:
`https://username.github.io/repo-name/`

## Features

- **Free hosting** via GitHub Pages
- **Free automation** with GitHub Actions
- **Free CDN** through raw.githubusercontent.com
- **Automatic versioning** of all data changes
- **Error handling** and retry logic
- **JSONP support** for cross-origin requests
- **Dashboard template** for data visualization

## Use Cases

- Weather data aggregation
- Stock market indicators
- Social media metrics
- Government data portals
- Environmental monitoring
- News aggregation
- Cryptocurrency prices

## Limitations

- Repository size: 1GB maximum
- GitHub Actions: 2,000 minutes/month (free tier)
- File size: 100MB maximum per file
- Update frequency: Recommend hourly minimum

## Documentation

For detailed setup instructions and examples, see the [complete guide](https://joel-hanson.github.io/posts/github-data-platform/).

## Contributing

1. Fork the repository
2. Create your feature branch
3. Submit a pull request

## License

MIT License - feel free to use for any purpose!

## Related Projects

- [Antarctic Iceberg Tracker](https://github.com/Joel-hanson/Iceberg-locations) - Real-world example
- [Weather API Template](https://github.com/Joel-hanson/weather-api-project) - Weather data example

---

**Ready to build your data platform?** Fork this repo and start customizing!
