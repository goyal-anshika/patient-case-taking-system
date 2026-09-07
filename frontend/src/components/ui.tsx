import type { ButtonHTMLAttributes, InputHTMLAttributes, ReactNode, SelectHTMLAttributes, TextareaHTMLAttributes } from 'react';
import { Loader2, ChevronDown, Check, AlertCircle, Info, Sparkles, UserRound, FileText, Stethoscope } from 'lucide-react';

export type ButtonVariant = 'primary' | 'secondary' | 'outline' | 'ghost' | 'danger' | 'success' | 'dark';
export type ButtonSize = 'sm' | 'md' | 'lg' | 'xl';

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant;
  size?: ButtonSize;
  loading?: boolean;
  icon?: ReactNode;
  iconRight?: ReactNode;
  fullWidth?: boolean;
}

export function Button({ variant = 'primary', size = 'md', loading = false, icon, iconRight, fullWidth = false, className = '', children, disabled, ...props }: ButtonProps) {
  const base = 'inline-flex items-center justify-center gap-2 rounded-xl font-semibold transition-all duration-200 focus:outline-none disabled:cursor-not-allowed disabled:opacity-50 active:scale-[0.98]';
  const variants: Record<ButtonVariant, string> = {
    primary: 'bg-teal-700 text-white hover:bg-teal-800 shadow-sm hover:shadow-md',
    secondary: 'bg-blue-600 text-white hover:bg-blue-700 shadow-sm hover:shadow-md',
    outline: 'border border-surface-300 bg-white text-surface-700 hover:border-teal-500 hover:bg-teal-50 hover:text-teal-700 dark:border-surface-700 dark:bg-surface-900 dark:text-surface-200 dark:hover:bg-teal-950/40',
    ghost: 'text-surface-600 hover:bg-surface-100 hover:text-surface-900 dark:text-surface-300 dark:hover:bg-surface-800 dark:hover:text-white',
    danger: 'bg-error-600 text-white hover:bg-error-700 shadow-sm',
    success: 'bg-success-600 text-white hover:bg-success-700 shadow-sm',
    dark: 'bg-surface-900 text-white hover:bg-surface-800 dark:bg-white dark:text-surface-900',
  };
  const sizes: Record<ButtonSize, string> = {
    sm: 'px-3 py-2 text-xs',
    md: 'px-4 py-2.5 text-sm',
    lg: 'px-5 py-3 text-sm',
    xl: 'px-7 py-4 text-base',
  };
  return (
    <button className={`${base} ${variants[variant]} ${sizes[size]} ${fullWidth ? 'w-full' : ''} ${className}`} disabled={disabled || loading} {...props}>
      {loading ? <Loader2 className="h-4 w-4 animate-spin" /> : icon}
      {children}
      {!loading && iconRight}
    </button>
  );
}

interface CardProps {
  children: ReactNode;
  className?: string;
  padding?: 'none' | 'sm' | 'md' | 'lg';
  hover?: boolean;
  onClick?: () => void;
}

export function Card({ children, className = '', padding = 'md', hover = false, onClick }: CardProps) {
  const paddings = { none: '', sm: 'p-4', md: 'p-5', lg: 'p-6 sm:p-7' };
  return <div className={`rounded-2xl border border-surface-200 bg-white shadow-card dark:border-surface-800 dark:bg-surface-900 ${paddings[padding]} ${hover ? 'transition-all duration-200 hover:-translate-y-0.5 hover:shadow-card-hover' : ''} ${onClick ? 'cursor-pointer' : ''} ${className}`} onClick={onClick}>{children}</div>;
}

export type BadgeTone = 'teal' | 'blue' | 'green' | 'amber' | 'red' | 'slate' | 'ai' | 'doctor';

interface BadgeProps { children: ReactNode; tone?: BadgeTone; dot?: boolean; icon?: ReactNode; className?: string; }

export function Badge({ children, tone = 'slate', dot = false, icon, className = '' }: BadgeProps) {
  const tones: Record<BadgeTone, string> = {
    teal: 'bg-teal-50 text-teal-700 border-teal-100 dark:bg-teal-950/50 dark:text-teal-300 dark:border-teal-900',
    blue: 'bg-blue-50 text-blue-700 border-blue-100 dark:bg-blue-950/50 dark:text-blue-300 dark:border-blue-900',
    green: 'bg-success-50 text-success-700 border-success-100 dark:bg-success-950/50 dark:text-success-300 dark:border-success-900',
    amber: 'bg-warning-50 text-warning-700 border-warning-100 dark:bg-warning-950/50 dark:text-warning-300 dark:border-warning-900',
    red: 'bg-error-50 text-error-700 border-error-100 dark:bg-error-950/50 dark:text-error-300 dark:border-error-900',
    slate: 'bg-surface-100 text-surface-600 border-surface-200 dark:bg-surface-800 dark:text-surface-300 dark:border-surface-700',
    ai: 'bg-teal-50 text-teal-700 border-teal-200 dark:bg-teal-950/50 dark:text-teal-300 dark:border-teal-800',
    doctor: 'bg-surface-800 text-white border-surface-800 dark:bg-surface-200 dark:text-surface-900 dark:border-surface-200',
  };
  return <span className={`inline-flex items-center gap-1.5 rounded-full border px-2.5 py-1 text-[11px] font-semibold ${tones[tone]} ${className}`}>{dot && <span className="h-1.5 w-1.5 rounded-full bg-current" />}{icon}{children}</span>;
}

interface InputProps extends InputHTMLAttributes<HTMLInputElement> { label?: string; hint?: string; error?: string; icon?: ReactNode; }
export function Input({ label, hint, error, icon, className = '', id, ...props }: InputProps) {
  const inputId = id || `input-${label?.toLowerCase().replace(/\s/g, '-')}`;
  return <div className="space-y-1.5"><>{label && <label htmlFor={inputId} className="block text-sm font-semibold text-surface-700 dark:text-surface-200">{label}{props.required && <span className="ml-1 text-error-500">*</span>}</label>}</><div className="relative">{icon && <span className="absolute left-3.5 top-1/2 -translate-y-1/2 text-surface-400">{icon}</span>}<input id={inputId} className={`w-full rounded-xl border bg-white px-3.5 py-3 text-sm text-surface-900 placeholder:text-surface-400 transition-all focus:border-teal-500 focus:ring-2 focus:ring-teal-100 dark:border-surface-700 dark:bg-surface-900 dark:text-white dark:focus:border-teal-500 dark:focus:ring-teal-950 ${icon ? 'pl-10' : ''} ${error ? 'border-error-400 focus:border-error-500 focus:ring-error-100' : 'border-surface-200'} ${className}`} {...props} /></div>{error ? <p className="flex items-center gap-1 text-xs text-error-600"><AlertCircle className="h-3.5 w-3.5" />{error}</p> : hint && <p className="text-xs text-surface-500">{hint}</p>}</div>;
}

interface SelectProps extends SelectHTMLAttributes<HTMLSelectElement> { label?: string; children: ReactNode; }
export function Select({ label, children, className = '', id, ...props }: SelectProps) { return <div className="space-y-1.5">{label && <label htmlFor={id} className="block text-sm font-semibold text-surface-700 dark:text-surface-200">{label}</label>}<div className="relative"><select id={id} className={`w-full appearance-none rounded-xl border border-surface-200 bg-white px-3.5 py-3 text-sm text-surface-900 focus:border-teal-500 focus:ring-2 focus:ring-teal-100 dark:border-surface-700 dark:bg-surface-900 dark:text-white ${className}`} {...props}>{children}</select><ChevronDown className="pointer-events-none absolute right-3.5 top-1/2 h-4 w-4 -translate-y-1/2 text-surface-400" /></div></div>; }

interface TextareaProps extends TextareaHTMLAttributes<HTMLTextAreaElement> { label?: string; }
export function Textarea({ label, className = '', id, ...props }: TextareaProps) { return <div className="space-y-1.5">{label && <label htmlFor={id} className="block text-sm font-semibold text-surface-700 dark:text-surface-200">{label}</label>}<textarea id={id} className={`w-full resize-y rounded-xl border border-surface-200 bg-white px-3.5 py-3 text-sm text-surface-900 placeholder:text-surface-400 focus:border-teal-500 focus:ring-2 focus:ring-teal-100 dark:border-surface-700 dark:bg-surface-900 dark:text-white ${className}`} {...props} /></div>; }

interface PageHeaderProps { eyebrow?: string; title: string; description?: string; action?: ReactNode; }
export function PageHeader({ eyebrow, title, description, action }: PageHeaderProps) { return <div className="mb-7 flex flex-col justify-between gap-4 sm:flex-row sm:items-end"> <div>{eyebrow && <p className="mb-1.5 text-xs font-bold uppercase tracking-widest text-teal-600">{eyebrow}</p>}<h1 className="text-2xl font-bold tracking-tight text-surface-900 dark:text-white sm:text-3xl">{title}</h1>{description && <p className="mt-1.5 text-sm text-surface-500 dark:text-surface-400">{description}</p>}</div>{action && <div className="shrink-0">{action}</div>}</div>; }

export function SectionHeading({ icon, title, description, action }: { icon?: ReactNode; title: string; description?: string; action?: ReactNode }) { return <div className="mb-4 flex items-center justify-between gap-3"><div className="flex items-center gap-3">{icon && <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-teal-50 text-teal-700 dark:bg-teal-950/50 dark:text-teal-300">{icon}</div>}<div><h2 className="font-jakarta text-base font-bold text-surface-900 dark:text-white">{title}</h2>{description && <p className="mt-0.5 text-xs text-surface-500">{description}</p>}</div></div>{action}</div>; }

export function EmptyState({ icon = <FileText className="h-6 w-6" />, title, description, action }: { icon?: ReactNode; title: string; description: string; action?: ReactNode }) { return <div className="flex flex-col items-center justify-center rounded-2xl border border-dashed border-surface-300 bg-surface-50/50 px-6 py-12 text-center dark:border-surface-700 dark:bg-surface-900/50"><div className="mb-3 flex h-12 w-12 items-center justify-center rounded-2xl bg-surface-100 text-surface-400 dark:bg-surface-800">{icon}</div><h3 className="font-semibold text-surface-800 dark:text-white">{title}</h3><p className="mt-1 max-w-xs text-sm text-surface-500">{description}</p>{action && <div className="mt-4">{action}</div>}</div>; }

export function SourceIcon({ source }: { source: string }) { const icons: Record<string, ReactNode> = { patient: <UserRound className="h-3 w-3" />, 'ai-extracted': <Sparkles className="h-3 w-3" />, document: <FileText className="h-3 w-3" />, 'doctor-entered': <Stethoscope className="h-3 w-3" /> }; return icons[source] ?? <Info className="h-3 w-3" />; }

export function SourceBadge({ source }: { source: 'patient' | 'ai-extracted' | 'document' | 'doctor-entered' | 'ai-summary' }) { const config = { patient: { label: 'Patient provided', tone: 'blue' as BadgeTone }, 'ai-extracted': { label: 'AI extracted', tone: 'ai' as BadgeTone }, document: { label: 'Document', tone: 'amber' as BadgeTone }, 'doctor-entered': { label: 'Doctor entered', tone: 'doctor' as BadgeTone }, 'ai-summary': { label: 'AI-assisted', tone: 'ai' as BadgeTone } }; const item = config[source]; return <Badge tone={item.tone} icon={<SourceIcon source={source} />}>{item.label}</Badge>; }

export function ProgressBar({ value, label, showValue = false }: { value: number; label?: string; showValue?: boolean }) { return <div className="space-y-1.5">{(label || showValue) && <div className="flex justify-between text-xs font-medium text-surface-500"><span>{label}</span>{showValue && <span>{value}%</span>}</div>}<div className="h-2 overflow-hidden rounded-full bg-surface-100 dark:bg-surface-800"><div className="h-full rounded-full bg-teal-600 transition-all duration-500" style={{ width: `${value}%` }} /></div></div>; }

export function Checkbox({ label, checked, onChange }: { label: ReactNode; checked: boolean; onChange: (checked: boolean) => void }) { return <label className="flex cursor-pointer items-start gap-3"><button type="button" role="checkbox" aria-checked={checked} onClick={() => onChange(!checked)} className={`mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-md border transition-colors ${checked ? 'border-teal-700 bg-teal-700 text-white' : 'border-surface-300 bg-white dark:border-surface-600 dark:bg-surface-800'}`}>{checked && <Check className="h-3.5 w-3.5" />}</button><span className="text-sm leading-6 text-surface-600 dark:text-surface-300">{label}</span></label>; }
