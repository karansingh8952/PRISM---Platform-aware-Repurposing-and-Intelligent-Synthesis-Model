import { useState } from 'react'
import { Upload, FileText, ArrowRight, Sparkles } from 'lucide-react'

const API = "http://127.0.0.1:8000"

function InputPage() {
  const [inputText, setInputText] = useState("")
  const [file, setFile] = useState(null)
  const [contentId, setContentId] = useState(null)
  const [extracted, setExtracted] = useState("")
  const [summary, setSummary] = useState("")
  const [loading, setLoading] = useState(false)
  const [summarizing, setSummarizing] = useState(false)
  const [error, setError] = useState("")

  const handleExtract = async () => {
    if (!inputText.trim() && !file) return

    setLoading(true)
    setError("")
    setExtracted("")
    setSummary("")
    setContentId(null)

    try {
      let response

      if (file) {
        if (!file.name.toLowerCase().endsWith(".pdf")) {
          throw new Error("Only PDF files are supported for upload right now.")
        }
        const formData = new FormData()
        formData.append("file", file)
        response = await fetch(`${API}/extract/pdf`, {
          method: "POST",
          body: formData,
        })
      } else if (/youtube\.com|youtu\.be/i.test(inputText)) {
        response = await fetch(`${API}/extract/youtube`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ url: inputText.trim() }), // check field name in /docs
        })
      } else {
        response = await fetch(`${API}/extract/text`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ text: inputText }),
        })
      }

      if (!response.ok) throw new Error(`Server error ${response.status}`)

      const data = await response.json()
      setContentId(data.id)
      setExtracted(data.extracted_text ?? data.raw_text ?? JSON.stringify(data, null, 2))
    } catch (err) {
      setError(err.message || "Couldn't connect — check the backend is running.")
    } finally {
      setLoading(false)
    }
  }

  const handleSummarize = async () => {
    if (!contentId) return

    setSummarizing(true)
    setError("")
    setSummary("")

    try {
      const response = await fetch(`${API}/summarize/${contentId}`, {
        method: "POST",
      })
      if (!response.ok) throw new Error(`Summarize failed: ${response.status}`)

      const data = await response.json()
      setSummary(
        data.summary ?? (typeof data === "string" ? data : JSON.stringify(data, null, 2))
      )
    } catch (err) {
      setError(err.message)
    } finally {
      setSummarizing(false)
    }
  }

  return (
    <div className="px-12 py-10 max-w-4xl mx-auto">
      <p className="text-sm text-[#4638E0] font-medium mb-2">Content Engine</p>
      <h1 className="font-display text-3xl font-semibold mb-1 text-[#15161A]">
        What are we repurposing today?
      </h1>
      <p className="text-sm text-gray-500 mb-8">
        Upload a PDF, paste text, or paste a YouTube link — PRISM handles the rest.
      </p>

      <div className="bg-white rounded-2xl shadow-sm border border-[#ECECEF] p-6">
        <textarea
          className="w-full h-32 text-sm resize-none focus:outline-none placeholder:text-gray-400"
          placeholder="Paste a blog post, transcript, or YouTube link..."
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
        />

        <div className="flex items-center justify-between pt-4 border-t border-[#F0F0F2] mt-4">
          <label className="flex items-center gap-2 text-sm text-gray-500 cursor-pointer hover:text-[#15161A] transition-colors">
            <Upload size={16} />
            {file ? file.name : "Attach PDF"}
            <input
              type="file"
              accept=".pdf,application/pdf"
              className="hidden"
              onChange={(e) => setFile(e.target.files[0] || null)}
            />
          </label>

          <button
            onClick={handleExtract}
            disabled={loading}
            className="flex items-center gap-2 bg-gradient-to-br from-[#6C5CE7] to-[#4638E0] text-white text-sm font-medium px-5 py-2.5 rounded-lg hover:opacity-90 transition-opacity disabled:opacity-50"
          >
            {loading ? "Extracting..." : "Generate"}
            <ArrowRight size={16} />
          </button>
        </div>

        {error && (
          <div className="mt-4 p-4 rounded-lg bg-red-100 text-red-700 border border-red-300 text-sm">
            {error}
          </div>
        )}

        {extracted && (
          <div className="mt-4 p-4 rounded-lg bg-[#F8F8FA] border border-[#ECECEF]">
            <div className="flex items-center justify-between mb-2">
              <h3 className="text-sm font-semibold text-[#15161A] flex items-center gap-2">
                <FileText size={14} />
                Extracted Text
              </h3>
              <button
                onClick={handleSummarize}
                disabled={summarizing}
                className="flex items-center gap-1.5 text-xs font-medium text-[#4638E0] hover:opacity-80 disabled:opacity-50"
              >
                <Sparkles size={14} />
                {summarizing ? "Summarizing..." : "Summarize"}
              </button>
            </div>
            <p className="text-sm text-gray-700 whitespace-pre-wrap max-h-64 overflow-y-auto">
              {extracted}
            </p>
          </div>
        )}

        {summary && (
          <div className="mt-4 p-4 rounded-lg bg-[#F1EFFE] border border-[#D9D4FA]">
            <h3 className="text-sm font-semibold mb-2 text-[#4638E0] flex items-center gap-2">
              <Sparkles size={14} />
              Summary
            </h3>
            <p className="text-sm text-gray-800 whitespace-pre-wrap">{summary}</p>
          </div>
        )}
      </div>
    </div>
  )
}

export default InputPage