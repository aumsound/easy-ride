# 🏍️ Misha's Bikes - Complete Website Package

## ✅ What You Get

1. **index.html** - Complete website with admin panel
2. **bikes-config.js** - All bikes data (10 Click, 10 NMAX, 3 XMAX)
3. **optimize-images.py** - Script to optimize photos
4. **This README** - Complete instructions

## 🚀 Quick Setup (5 minutes)

### Step 1: Prepare Photos
1. Create folder `original_images/`
2. Add bike photos named: `1.jpg`, `2.jpg`, ... `23.jpg`
   - 1-10: Honda Click bikes
   - 11-20: Yamaha NMAX bikes
   - 21-23: Yamaha XMAX bikes

### Step 2: Optimize Photos
```bash
# Install Python package (one time only)
pip install Pillow

# Run optimization
python optimize-images.py
```
This creates `images/` folder with optimized photos.

### Step 3: Deploy to GitHub
1. Create new repository on GitHub
2. Upload all files:
   - `index.html`
   - `bikes-config.js`
   - `images/` folder with all photos
3. Go to Settings → Pages → Enable GitHub Pages
4. Your site is live at: `https://[username].github.io/[repo-name]`

## 👨‍💼 Admin Panel

### Access
- URL: `yoursite.com#admin`
- Username: **admin**
- Password: **misha2025**

### Features
- ✅ Turn bikes on/off
- ✅ Set rental/sale status
- ✅ Edit prices (day/month/sale)
- ✅ Update year and mileage
- ✅ Export/import configuration

### How It Works
1. Login to admin panel
2. Check/uncheck boxes to show/hide bikes
3. Edit prices directly in fields
4. Click "Save Changes" to apply
5. Click "Export Config" to backup

## 📱 WhatsApp Setup

Current number in code: **+7 917 555 6789**

### To Change WhatsApp Number:
1. Open `index.html` in any text editor
2. Press Ctrl+F (or Cmd+F on Mac)
3. Find: `79175556789`
4. Replace with: `[your-number]` (no spaces/symbols)
5. Save and upload

Example: For +66 95 123 4567, use: `66951234567`

## 🖼️ Photo Guidelines

### Naming Convention
- **MUST** be named exactly: `1.jpg`, `2.jpg`, etc.
- Number matches bike ID in config
- Use lowercase `.jpg` extension

### Photo Tips
- Take photos at same angle for consistency
- Clean bikes before shooting
- Good lighting (morning/evening best)
- Include full bike in frame
- 16:9 aspect ratio works best

## 💾 Configuration Management

### Method 1: Through Admin Panel (Easy)
1. Login to admin panel
2. Make changes
3. Click "Save Changes"
4. Click "Export Config" to download backup

### Method 2: Edit bikes-config.js (Advanced)
```javascript
{
  "id": 1,              // Don't change
  "number": "1",        // Bike number
  "price_day": 250,     // Daily price in THB
  "price_month": 5000,  // Monthly price in THB
  "sale_price": 45000,  // Sale price in THB
  "year": 2023,         // Year
  "mileage": 5000,      // Kilometers
  "for_rent": true,     // Show in rentals
  "for_sale": false,    // Show in for sale
  "active": true        // Show on website
}
```

## 🔍 Testing Checklist

Before going live:
- [ ] All 23 bike photos uploaded
- [ ] WhatsApp number updated
- [ ] Test on mobile phone
- [ ] Test WhatsApp links
- [ ] Test admin panel login
- [ ] Check all bikes display correctly
- [ ] Test rental/sale toggle

## 🚨 Troubleshooting

### Photos not showing?
- Check file names: must be `1.jpg`, not `1.JPG` or `01.jpg`
- Check images folder exists
- Clear browser cache (Ctrl+Shift+R)

### Admin panel not working?
- Make sure URL has `#admin` at end
- Username: admin (lowercase)
- Password: misha2025 (lowercase)
- Try different browser

### Changes not saving?
- Click "Save Changes" button
- Export config for backup
- Check browser allows localStorage

## 📲 Mobile Preview

The site is mobile-first and will look great on phones. Main features:
- Fast loading
- Swipeable bike galleries
- One-tap WhatsApp booking
- Easy navigation

## 🎯 Final Steps for Misha

1. **Add Photos**: Name them 1.jpg to 23.jpg
2. **Optimize**: Run the Python script
3. **Update WhatsApp**: Replace number in index.html
4. **Upload**: Push to GitHub/hosting
5. **Test**: Check everything works on phone
6. **Share**: Send link to customers!

## 💡 Pro Tips

1. **Regular Backups**: Export config weekly
2. **Photo Updates**: Keep originals in separate folder
3. **Price Updates**: Can be done from any device through admin
4. **Seasonal Changes**: Easy to mark bikes as unavailable

## 📞 Need Help?

If something doesn't work:
1. Check this README first
2. Look at browser console (F12 → Console)
3. Make sure all files are uploaded
4. Try clearing cache

---

**Ready to go! The site is fully functional and waiting for your photos.** 🚀

*Remember: This is a static site with browser storage. For more features (online payments, booking calendar, etc.), you'll need a backend server.*