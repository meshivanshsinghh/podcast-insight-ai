# PodcastInsight 🎙️ 
### AI-Powered Podcast Analytics Platform

## Overview 🚀
PodcastInsight transforms podcast analysis through AssemblyAI's advanced speech recognition. Built for the AssemblyAI Hackathon, it helps creators and managers understand their content better through detailed speaker analysis, content structure, and engagement metrics.

## Key Features & Implementation ✨

### 1. Speaker Analysis 🗣️
**What it does:**
- Identifies different speakers in a podcast
- Tracks speaking time for each participant
- Analyzes speaking patterns

**Example:**
```plaintext
For a Joe Rogan podcast episode:
- "Joe spoke 60% of the time"
- "Guest interrupted 5 times"
- "Average segment length: 2.5 minutes"
```

### 2. Content Timeline 📊
**What it does:**
- Interactive, color-coded timeline
- Click to jump to specific moments
- Hover to see transcripts

**Example:**
```plaintext
Timeline shows:
- Red segments for Speaker 1
- Blue segments for Speaker 2
- Yellow highlights for key moments
- Tooltips with text on hover
```

### 3. Topic Analysis 📈
**What it does:**
- Automatically detects main topics
- Creates chapter markers
- Generates topic word clouds

**Example:**
```plaintext
For a tech podcast:
- Chapter 1: "Introduction to AI" (0:00-15:30)
- Chapter 2: "Future of Technology" (15:30-35:45)
- Common topics: AI, Machine Learning, Innovation
```

### 4. Quality Metrics 📑
**What it does:**
- Measures content clarity
- Identifies key moments
- Analyzes conversation flow

**Example:**
```plaintext
Episode Insights:
- Clear speech: 95%
- Key moments: 5 identified
- Natural conversation flow: High
```

## Tech Stack 🛠️

### Core Technologies
- Python 3.9+
- AssemblyAI API (Speech-to-Text & Audio Intelligence)
- Streamlit (UI Framework)
- Plotly (Interactive Visualizations)

### Key Libraries
```python
assemblyai==0.19.0    # Speech recognition
streamlit==1.31.0     # Web interface
plotly==5.18.0        # Data visualization
pandas==2.2.0         # Data processing
python-dotenv==1.0.0  # Environment management
```

## Quick Start 🚀

1. **Setup**
```bash
git clone https://github.com/yourusername/podcast-insight.git
cd podcast-insight
pip install -r requirements.txt
```

2. **Configuration**
```bash
# Add to .env file:
ASSEMBLYAI_API_KEY=your_api_key_here
```

3. **Run**
```bash
streamlit run app.py
```

## How To Use 💡

1. **Input**
   - Paste YouTube URL of any podcast episode
   - Supports episodes up to 2 hours
   - Works with multiple speakers

2. **Analysis**
   - System processes audio
   - Generates interactive visualizations
   - Creates downloadable insights

3. **Results**
   - View interactive dashboard
   - Explore speaker patterns
   - Download detailed reports

## Implementation Details 🔍

### Core Features (All Implemented)
1. **Upload & Process**
   - YouTube URL input
   - Progress tracking
   - Error handling

2. **Speaker Analysis**
   - Speaker diarization
   - Time distribution
   - Interaction patterns

3. **Interactive Visuals**
   - Timeline view
   - Speaker charts
   - Topic clouds

4. **Smart Analytics**
   - Quality metrics
   - Key moments
   - Engagement tracking

### Visualization Types
1. **Timeline View**
   - Multi-speaker timeline
   - Interactive segments
   - Timestamp navigation

2. **Analytics Charts**
   - Speaker distribution
   - Topic frequency
   - Engagement patterns

## Use Cases 📱

### Podcast Creators
- Track speaker balance
- Identify engaging segments
- Optimize content structure

### Content Managers
- Assess episode quality
- Monitor speaker dynamics
- Generate show notes

## Technical Requirements ⚙️
- Python 3.9 or higher
- AssemblyAI API key
- Internet connection
- 4GB RAM minimum

## License 📝
MIT License

## Acknowledgments 🙏
- Built with AssemblyAI's Universal-2 model
- Created for AssemblyAI Hackathon 2024

## Contact 📬
- Your Name
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

---
### Built with AssemblyAI 🎙️ Crafted with ❤️