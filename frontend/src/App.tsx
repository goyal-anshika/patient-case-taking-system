import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom';
import { LandingPage } from '@/pages/landing';
import { CompletePage, ConsentPage, ConversationPage, DocumentsPage, LanguagePage, PatientWelcome, RegisterPage, SummaryPage, VerifyPage } from '@/pages/patient';
import { DoctorDashboard, DoctorLogin, PatientCasePage, PatientListPage, SettingsPage } from '@/pages/doctor';

function App() {
  return <BrowserRouter><Routes>
    <Route path="/" element={<LandingPage />} />
    <Route path="/patient" element={<PatientWelcome />} />
    <Route path="/patient/language" element={<LanguagePage />} />
    <Route path="/patient/register" element={<RegisterPage />} />
    <Route path="/patient/consent" element={<ConsentPage />} />
    <Route path="/patient/conversation" element={<ConversationPage />} />
    <Route path="/patient/documents" element={<DocumentsPage />} />
    <Route path="/patient/verify" element={<VerifyPage />} />
    <Route path="/patient/summary" element={<SummaryPage />} />
    <Route path="/patient/complete" element={<CompletePage />} />
    <Route path="/doctor/login" element={<DoctorLogin />} />
    <Route path="/doctor/dashboard" element={<DoctorDashboard />} />
    <Route path="/doctor/patients" element={<PatientListPage />} />
    <Route path="/doctor/patients/:id" element={<PatientCasePage />} />
    <Route path="/doctor/patients/:id/:tab" element={<PatientCasePage />} />
    <Route path="/doctor/queue" element={<PatientListPage />} />
    <Route path="/doctor/cases" element={<PatientListPage />} />
    <Route path="/doctor/documents" element={<PatientListPage />} />
    <Route path="/doctor/consultations" element={<PatientListPage />} />
    <Route path="/doctor/settings" element={<SettingsPage />} />
    <Route path="*" element={<Navigate to="/" replace />} />
  </Routes></BrowserRouter>;
}

export default App;
